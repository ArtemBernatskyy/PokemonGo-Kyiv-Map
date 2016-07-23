from django.shortcuts import render
import geopy
import geopy.distance
from functools import reduce
from .bigdata.data import kyiv_points, kyiv_polygon


# ///////////////////////////////////////////////////
TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def cmp(a, b):
    return (a > b) - (a < b) 

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    """Returns points on convex hull of an array of points in CCW order."""
    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


# ///////////////////////////////////////////

ccoordinate_list = kyiv_points
starting_coordinate = (50.4501, 30.5234)

def poke_players_places(coordinate, ccoordinate_list):
	export_material = []	# here will be list of lists in every list there will be locations for one player to scan
	
	for player in range(400):
		pts = [ geopy.Point(p[0],p[1]) for p in ccoordinate_list ]
		onept = geopy.Point(coordinate[0],coordinate[1])
		alldist = [ (p,geopy.distance.distance(p, onept).km) for p in pts ]
		nearest_points = sorted(alldist, key=lambda x: (x[1]))[:99]

		# converting to normal view
		player_list = []
		for point in nearest_points:
			player_list.append([point[0].longitude, point[0].latitude])

		# delete our set coordinates from database
		# print(len(ccoordinate_list), len(player_list))
		for delete_value in player_list:
			delete_value = [delete_value[1], delete_value[0]]
			# print(delete_value)
			if delete_value in ccoordinate_list:
				i = ccoordinate_list.index(delete_value)
				del ccoordinate_list[i]

		# optionaly return sorted coordinates by graham algorythm for poligon visualisation
		player_list = convex_hull(player_list)
		export_material.append([player_list])
		# changing starting point
		if len(ccoordinate_list) == 0:
			break	# it means that we out of coordinates to draw
		coordinate = ccoordinate_list[0]
		# print(len(ccoordinate_list))

	# print(export_material)
	return export_material

# Create your views here.
def map(request):
	context = {
	'data': kyiv_points
	}

	return render(request, "mapview/map.html", context)


def polygon(request):
	kyiv_points = poke_players_places(starting_coordinate, ccoordinate_list)

	context = {
	'kyiv_polygon': kyiv_polygon,
	'kyiv_points': kyiv_points
	}

	return render(request, "mapview/polygon.html", context)