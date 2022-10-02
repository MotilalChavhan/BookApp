from django.contrib import admin
from .models import Member, Book, Transaction

admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Transaction)
