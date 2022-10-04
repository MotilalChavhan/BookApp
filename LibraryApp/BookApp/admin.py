from django.contrib import admin
from .models import Member, Book, Transaction

class BookAdmin(admin.ModelAdmin):
	list_display = ['id', 'member', 'title', 'authors', 'isbn', 'publisher']

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['id', 'member', 'book', 'date', 'action', 'fees']

admin.site.register(Member)
admin.site.register(Book, BookAdmin)
admin.site.register(Transaction, TransactionAdmin)
