#!/usr/bin/env python3

import pprint
import struct
from pgoapi import pgoapi
from geopy.geocoders import GoogleV3
from s2sphere import Cell, CellId, LatLng

def f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]

def get_cell_ids(lat, long, radius=10):
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(15)
    walk = [origin.id()]
    right = origin.next()
    left = origin.prev()

    for i in range(radius):
        walk.append(right.id())
        walk.append(left.id())
        right = right.next()
        left = left.prev()

    return sorted(walk)

geolocator = GoogleV3()
loc = geolocator.geocode('50.448178, 30.460203', timeout=10)

api = pgoapi.PGoApi()
api.set_position(loc.latitude, loc.longitude, loc.altitude)
api_login_result = False
while not api_login_result:
    try:
        api_login_result = api.login('ptc', 'sds8828282', 'dsdsd32232')
    except ValueError:
        api_login_result = False
        print('Unexpected login exception')
    print(api_login_result)
print('Login success')


def scan(loc_str):
    pokemons = []
    loc = geolocator.geocode(loc_str, timeout=10)
    cell_ids = get_cell_ids(loc.latitude, loc.longitude)
    timestamps = [0,] * len(cell_ids)
    api.get_map_objects(latitude=f2i(loc.latitude), longitude=f2i(loc.longitude), since_timestamp_ms=timestamps, cell_id=cell_ids)
    response_dict = api.call()
    for map_cell in response_dict['responses']['GET_MAP_OBJECTS']['map_cells']:
        if 'catchable_pokemons' in map_cell.keys():
            for pokemon in map_cell['catchable_pokemons']:
                # print(pokemon)
                pass
                # pokemons.append(pokemon)
            pokemons.extend(map_cell['catchable_pokemons'])
    return pokemons



#######################
# def spiral(step):
main_pokemons = []
step = 10
x = y = 0
gx = float(50.448178)  # google coordinates
gy = float(30.460203)  # google coordinates
ddx = 0
ddy = -0.005
dx = 0
dy = -1
for i in range(step**2):
    if (-step/2 < x <= step/2) and (-step/2 < y <= step/2):
        # print ("{0:.4f}".format(gx), "{0:.4f}".format(gy))
        loc_str = "{0:.12f}".format(gx) + ', ' + "{0:.12f}".format(gy)
        print(loc_str)
        main_pokemons.extend(scan(loc_str))
        print(len(main_pokemons))
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
        ddx, ddy = -ddy, ddx
    x, y = x+dx, y+dy
    gx, gy = gx+ ddx, gy + ddy