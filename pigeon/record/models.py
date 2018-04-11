from django.db import models

# Create your models here.

class Pigeon_family(models.Model):
	name = models.CharField(max_length=20, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name		
	class Meta:
		ordering = ('created',)

class Pigeon(models.Model):
	name = models.CharField(max_length=20, unique=True)
	dad = models.CharField(max_length=20, blank=True)
	mom = models.CharField(max_length=20, blank=True)
	family = models.ForeignKey('Pigeon_family', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ('created',)

