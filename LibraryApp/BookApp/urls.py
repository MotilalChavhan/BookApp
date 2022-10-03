from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
	path("", views.landing, name="landing"),
	path("addbooks", views.addbooks, name="addbooks"),
	path("addmembers", views.addmembers, name="addmembers"),
	path("issuebooks", views.issuebooks, name="issuebooks"),
	path("returnbooks", views.returnbooks, name="returnbooks"),
	path("getbooks", views.getbooks, name="getbooks")
]