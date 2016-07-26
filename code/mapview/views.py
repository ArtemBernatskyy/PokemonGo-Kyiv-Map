from django.shortcuts import render
from .utils.functions import get_pokemons_from_cache
from django.views.decorators.cache import cache_page
from .tasks import player_scan
from .models import Player, City


# @cache_page(60)
def polygon(request):
	pokemons = get_pokemons_from_cache()

	context = {
		'pokemons': pokemons,
		# 'cities': City.objects.active(),
		# 'players': Player.objects.active(),
	}

	return render(request, "mapview/map.html", context)