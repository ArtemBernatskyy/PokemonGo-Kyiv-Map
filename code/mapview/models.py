from django.db import models

# Create your models here.
class PlayerManager(models.Manager):
    def active_and_lazy(self, *args, **kwargs):
        return super(PlayerManager, self).filter(state=True, is_celery_run=False)



class Player(models.Model):
	LOGIN_CHOICES = (
		(1, 'Success: Login'),
		(0, 'Failed/Error'),
		(None, 'Unknown/Inactive')
	)
	name = models.CharField(max_length=550, unique=True)
	email = models.CharField(blank=True, null=True, max_length=550)
	password = models.CharField(max_length=550)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	state = models.BooleanField(default=False, help_text='if true than this user will be active and will scan his square')
	is_celery_run = models.BooleanField(default=False, help_text='if celery is running this process already')
	can_login = models.IntegerField(choices=LOGIN_CHOICES, blank=True, null=True, verbose_name='login status') 
	description = models.CharField(max_length=550, blank=True, null=True, help_text='descripe this player, and the area for which he is responsible for')

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