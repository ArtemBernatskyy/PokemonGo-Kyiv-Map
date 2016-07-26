### TO START FRESHY ---------------------------------------------------------/

# celery start scipt to send tasks for workers
from mapview.tasks import player_scan
from mapview.models import Player

# resetting all players to default state (login unknnow and celery run false)
reset_players = Player.objects.all()
for player in reset_players:
	player.can_login = None
	player.is_celery_run = False
	player.save()


print('::::Sending tasks for workers')
players = Player.objects.active_and_lazy()
for player in players:
	player_scan.delay(player.pk)
	print('::::One more task')


### TO ADD TASK FOR NEW ACTIVE PLAYER ONLY ----------------------------------/
from mapview.tasks import player_scan
from mapview.models import Player


print('::::Sending tasks for workers')
players = Player.objects.active_and_lazy()
for player in players:
	player_scan.delay(player.pk)
	print('::::One more task')