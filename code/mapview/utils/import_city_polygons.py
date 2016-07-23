from mapview.utils.data import kyiv_polygon
from django.db import models
from mapview.models import *

for point in kyiv_polygon:
	CityPoint(city=City.objects.get(pk=1), lon=point[0], lat=point[1]).save()
	print(point)