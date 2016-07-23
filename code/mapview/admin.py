from django.contrib import admin

# Register your models here.
from .models import Player, PlayerPoint

class PlayerPointAdmin(admin.ModelAdmin):
    list_filter = ('player',)
    list_display = ['lat', 'lon', 'player']


admin.site.register(Player)
admin.site.register(PlayerPoint, PlayerPointAdmin)