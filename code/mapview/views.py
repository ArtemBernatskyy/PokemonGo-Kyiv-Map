from django.shortcuts import render
from .models import Player, City


def polygon(request):
	kyiv_points = ''

	context = {
		'cities': City.objects.active(),
		'players': Player.objects.active(),
	}

	return render(request, "mapview/map.html", context)