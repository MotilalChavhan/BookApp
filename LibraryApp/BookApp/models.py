import datetime
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

def get_sentinel_user():
    return Member.objects.get_or_create(username='deleted')[0]

def get_sentinel_book():
    return Book.objects.get_or_create(title='deleted')[0]

class Transaction(models.Model):
	member = models.ForeignKey(Member, null=True, on_delete=models.SET(get_sentinel_user))
	book = models.ForeignKey(Book, null=True, on_delete=models.SET(get_sentinel_book))
	date = models.DateField(default=datetime.date.today)
	action = models.CharField(max_length=20)
	fees = models.CharField(max_length=20, blank=True)

	def __str__(self):
		if self.action == 'issue':
			return f"{self.member.username} issued {self.book.title}"
		return f"{self.member.username} issued {self.book.title}"