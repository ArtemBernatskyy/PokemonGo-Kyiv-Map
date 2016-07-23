from django.shortcuts import render
import geopy
import geopy.distance
from .bigdata.data import kyiv_points, kyiv_polygon
from .utils import convex_hull



ccoordinate_list = kyiv_points
starting_coordinate = (50.4501, 30.5234)

def poke_players_places(coordinate, ccoordinate_list):
	export_material = []	# here will be list of lists in every list there will be locations for one player to scan
	
	for player in range(1):
		pts = [ geopy.Point(p[0],p[1]) for p in ccoordinate_list ]
		onept = geopy.Point(coordinate[0],coordinate[1])
		alldist = [ (p,geopy.distance.distance(p, onept).km) for p in pts ]
		nearest_points = sorted(alldist, key=lambda x: (x[1]))[:99]

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

		
		# player_list = convex_hull(player_list)	# For displaying as polygons
		export_material.append([player_list])
		# changing starting point
		if len(ccoordinate_list) == 0:
			break	# it means that we out of coordinates to draw
		coordinate = ccoordinate_list[0]

	return export_material	# return export_material[:-30]


def polygon(request):
	kyiv_points = poke_players_places(starting_coordinate, ccoordinate_list)

	context = {
	'kyiv_polygon': kyiv_polygon,
	'kyiv_points': kyiv_points
	}

	return render(request, "mapview/map.html", context)