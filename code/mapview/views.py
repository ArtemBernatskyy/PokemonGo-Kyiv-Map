from django.shortcuts import render
from .models import Player


def polygon(request):
	kyiv_points = ''

	context = {
		# 'kyiv_polygon': kyiv_polygon,
		'players': Player.objects.active()
	}

	return render(request, "mapview/map.html", context)