from django.db import models

# Create your models here.
class User(models.Model):
	id = models.IntegerField(primary_key=True)
	email = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	password = models.CharField(max_length=128)
	
	def __str__(self):
		return self.name
