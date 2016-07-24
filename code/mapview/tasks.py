from __future__ import absolute_import
from celery import shared_task
from celery.decorators import task
from time import sleep
from pgoapi import PGoApi
from pgoapi.utilities import f2i, h2f
from django.core.cache import cache
# from google.protobuf.internal import encoder
# from geopy.geocoders import GoogleV3
from s2sphere import Cell, CellId, LatLng
from mapview.models import Player, City


def get_cell_ids(lat, long, radius = 10):
	origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(15)
	walk = [origin.id()]
	right = origin.next()
	left = origin.prev()
	# Search around provided radius
	for i in range(radius):
		walk.append(right.id())
		walk.append(left.id())
		right = right.next()
		left = left.prev()

	# Return everything
	return sorted(walk)


@app.task
def player_area(id):
	player = Player.objects.get(id=id)
	cache_name = player.name
	api = PGoApi()
	api.set_position(player.points.all()[0].lat, player.points.all()[0].lon, 0.0)
	api.get_player()
	api_login_result = False
	while not api_login_result:
		try:
			api_login_result = api.login('ptc', player.name, player.password)
		except ValueError:
			api_login_result = False

	database_counter = 2	# indicates after how many cycles we check player state Activer or Passive
	player_state = Player.objects.get(id=id).state
	while player_state == True:
		for i, tile in enumerate(player.points.all()):
			api.set_position(tile.lat, tile.lon, 0.0)
			print('Step {0}'.format(i))
			cell_ids = get_cell_ids(tile.lat, tile.lon)
			timestamps = [0,] * len(cell_ids)
			api.get_map_objects(
				latitude=f2i(tile.lat), 
				longtitude=f2i(tile.lon), 
				since_timestamp_ms=timestamps, 
				cell_id=cell_ids
				)

			response_dict = api.call()
			for map_cell in response_dict['responses']['GET_MAP_OBJECTS']['map_cells']:
				if 'catchable_pokemons' in map_cell.keys():
					for pokemon in map_cell['catchable_pokemons']:
						print(pokemon)
						cache.add('pokemon_{0}'.format(pokemon['encounter_id']), pokemon)

			# sleep(5)
		database_counter -= 1
		if database_counter < 0:	# then updating state from database
			player_state = Player.objects.get(id=id).state
			database_counter = 2