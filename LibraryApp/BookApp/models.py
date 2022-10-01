from django.db import models

class Member(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	username = models.CharField(max_length=128, unique=True)
	email = models.EmailField(max_length=128, unique=True)

	def __str__(self):
		return self.username

class Book(models.Model):
	member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=128)
	authors = models.CharField(max_length=256)
	isbn = models.CharField(max_length=128)
	publisher = models.CharField(max_length=256)

	def __str__(self):
		return self.title