from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
	path("", views.landing, name="landing"),
	path("addbook", views.addbook, name="addbook"),
	path("addbooks", views.addbooks, name="addbooks"),
	path("addmembers", views.addmembers, name="addmembers"),
	path("issuebooks", views.issuebooks, name="issuebooks"),
	path("returnbooks", views.returnbooks, name="returnbooks"),
	path("getbooks", views.getbooks, name="getbooks"),
	path("books", views.books, name="books"),
	path("members", views.members, name="members"),
	path("deletebook", views.deletebook, name="deletebook"),
	path("editbook/<int:book_id>", views.editbook, name='editbook'),
	path("deletemember", views.deletemember, name="deletemember")
]