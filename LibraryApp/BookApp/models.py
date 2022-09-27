from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

class Book(models.Model):
	member = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=128)
	authors = models.CharField(max_length=256)
	isbn = models.CharField(max_length=128)
	publisher = models.CharField(max_length=256)

	def __str__(self):
		return self.title