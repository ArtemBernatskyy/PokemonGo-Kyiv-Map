from django.db import models

# Create your models here.


class Player(models.Model):
	name = models.CharField(max_length=550)
	email = models.CharField(blank=True, null=True, max_length=550)
	password = models.CharField(max_length=550)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class PlayerPoint(models.Model):
	player = models.ForeignKey(Player, related_name='points')
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)

	def __str__(self):
		return str(self.lat) + ', ' + str(self.lon)
