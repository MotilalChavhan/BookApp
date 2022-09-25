from django.urls import path
from . import views

urlpatterns = [
	path("", views.landing, name="landing"),
	path("addbooks", views.addbooks, name="addbooks"),
	path("addmembers", views.addmembers, name="addmembers"),
	path("issuebooks", views.issuebooks, name="issuebooks")
]