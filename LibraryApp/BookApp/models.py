from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
	title = models.CharField(max_length=128)
	authors = models.CharField(max_length=256)
	isbn = models.CharField(max_length=128)
	publisher = models.CharField(max_length=256)
	issued = models.BooleanField(default=False)

class User(AbstractUser):
	issued_books = models.ForeignKey(Book, blank=True, on_delete=models.CASCADE)


