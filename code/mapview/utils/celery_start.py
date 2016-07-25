# celery start scipt to send tasks for workers

from mapview.tasks import player_scan
from mapview.models import Player


print('::::Sending tasks for workers')
players = Player.objects.active()
for player in players:
	player_scan.delay(player.pk)
	print('::::One more task')