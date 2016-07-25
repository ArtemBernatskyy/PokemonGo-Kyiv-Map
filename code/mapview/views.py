from django.shortcuts import render
# from .utils.functions import get_pokemons_from_cache
# from django.views.decorators.cache import cache_page
from django.core.cache import cache
# from .tasks import player_scan
from .models import Player, City



# celery start scipt to send tasks for workers
# from mapview.tasks import player_scan
# from mapview.models import Player
# print('::::Sending tasks for workers')
# players = Player.objects.active()
# for player in players:
# 	player_scan.delay(player.pk)
# 	print('::::One more task')


# @cache_page(15)
def polygon(request):
	pokemons_list = []
	name_list = []
	pokemons_in_cache = cache.iter_keys("pokemon_*")
	for pokemon_in_cache in pokemons_in_cache:
		name_list.append(str(pokemon_in_cache))
		# pokemons_list.append(cache.get(str(pokemon_in_cache)))
	temp_list = cache.get_many(name_list)

	for key, pokemon_data in temp_list.items():
		pokemon_data.update({'image': '/static/mapview/icons/{0}.png'.format(str(pokemon_data['pokemon_id']))})

		pokemons_list.append(pokemon_data)
	pokemons = pokemons_list

	context = {
		'pokemons': pokemons,
	}

	return render(request, "mapview/map.html", context)