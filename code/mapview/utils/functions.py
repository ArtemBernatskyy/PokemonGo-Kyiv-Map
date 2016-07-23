from functools import reduce


def generate_map():
	main_pokemons = []
	step = 240
	x = y = 0
	gx = float(50.4501)  # google coordinates
	gy = float(30.5234)  # google coordinates
	ddx = 0
	ddy = -0.0025
	dx = 0
	dy = -1
	for i in range(step**2):
	    if (-step/2 < x <= step/2) and (-step/2 < y <= step/2):
	        # print ("{0:.4f}".format(gx), "{0:.4f}".format(gy))
	        loc_str = "{0:.12f}".format(gx) + ', ' + "{0:.12f}".format(gy)
	        # print(loc_str)
	        main_pokemons.append([gx, gy])
	        # print(len(main_pokemons))
	    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
	        dx, dy = -dy, dx
	        ddx, ddy = -ddy, ddx
	    x, y = x+dx, y+dy
	    gx, gy = gx+ ddx, gy + ddy
	    # print(i, 'from', step**2)

	return main_pokemons


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