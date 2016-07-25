from django.shortcuts import render
from .utils.functions import get_pokemons_from_cache
from .tasks import player_scan
from .models import Player, City

# celery start scipt to send tasks for workers
# from mapview.tasks import player_scan
# from mapview.models import Player
# print('::::Sending tasks for workers')
# players = Player.objects.active()
# for player in players:
# 	player_scan.delay(player.pk)
# 	print('::::One more task')



def polygon(request):
	pokemons = get_pokemons_from_cache()
	# player_area.delay(2)
	context = {
		'pokemons': pokemons,
		'cities': City.objects.active(),
		# 'players': Player.objects.active(),
	}

	return render(request, "mapview/map.html", context)