from django.db import models

# Create your models here.
class PlayerManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PlayerManager, self).filter(state=True)



class Player(models.Model):
	name = models.CharField(max_length=550, unique=True)
	email = models.CharField(blank=True, null=True, max_length=550)
	password = models.CharField(max_length=550)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	state = models.BooleanField(default=False, help_text='if true than this user will be active')

	objects = PlayerManager()

	class Meta:
		ordering = ('created_date',)

	def __str__(self):
		return self.name


class PlayerPoint(models.Model):
	player = models.ForeignKey(Player, related_name='points')
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.lat) + ', ' + str(self.lon)


class CityManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(CityManager, self).filter(state=True)


class City(models.Model):
	city_name = models.CharField(max_length=550, unique=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	state = models.BooleanField(default=False, help_text='if true than this user will be active')

	objects = PlayerManager()

	def __str__(self):
		return self.city_name


class CityPoint(models.Model):
	city = models.ForeignKey(City, related_name='points')
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.lat) + ', ' + str(self.lon)