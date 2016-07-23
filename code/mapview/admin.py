from django.contrib import admin

# Register your models here.
from .models import Player, PlayerPoint


admin.site.register(Player)
admin.site.register(PlayerPoint)