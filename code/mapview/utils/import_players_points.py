import geopy
import geopy.distance
from django.db import models
from mapview.models import *
from mapview.utils.functions import convex_hull
from mapview.utils.data import kyiv_points as ccoordinate_list

coordinate = (50.4501, 30.5234)

'''
%autoindent to disable indents in ipython
EXECUTE script from the manage.py level directory
'''


for player_id in range(400):
	pts = [ geopy.Point(p[0],p[1]) for p in ccoordinate_list ]
	onept = geopy.Point(coordinate[0],coordinate[1])
	alldist = [ (p,geopy.distance.distance(p, onept).km) for p in pts ]
	nearest_points = sorted(alldist, key=lambda x: (x[1]))[:600]

	# converting to normal view
	player_list = []
	for point in nearest_points:
		player_list.append([point[0].longitude, point[0].latitude])

	# delete our set coordinates from database
	for delete_value in player_list:
		delete_value = [delete_value[1], delete_value[0]]
		if delete_value in ccoordinate_list:
			i = ccoordinate_list.index(delete_value)
			del ccoordinate_list[i]
	
	# database stuff
	player = Player(name=str(player_id), password=str(player_id)*3)	# creating new player with nameand password
	player.save()													# saving player for one to many relations

	for point in player_list:
		PlayerPoint(player=Player.objects.get(pk=player.pk), lat=point[1], lon=point[0]).save()

	# changing starting point
	if len(ccoordinate_list) == 0:
		break	# it means that we out of coordinates to draw
	coordinate = ccoordinate_list[0]
	print('!!!!!!!!!!!!!!!!!!!!!!', player_id)
