from django.contrib import admin

# Register your models here.
from .models import (
	Player, PlayerPoint,
	City, CityPoint,
	)

class PlayerPointAdmin(admin.ModelAdmin):
    list_filter = ('player',)
    list_display = ['lat', 'lon', 'player']

class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('state',)


admin.site.register(City)
admin.site.register(CityPoint)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerPoint, PlayerPointAdmin)