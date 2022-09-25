import json
import requests
from django.shortcuts import render

def landing(request):
	return render(request, "landing.html")

def getbooks(request):
	url = "https://frappe.io/api/method/frappe-library"
	# data = json.load(request)
	payload = {
		"title" : request.POST['title'],
		"authors" : request.POST['authors'],
		"isbn" : request.POST['isbn'],
		"publisher" : request.POST['publisher'],
		"page" : request.POST['page'] 
	}
	response = requests.request("POST", url, json=payload)
	return render(request, "books_view.html", {
		"books" : response.json()["message"]
	})

def addbooks(request):
	return render(request, "books_view.html")

def addmembers(request):
	return render(request, "members_view.html")

def issuebooks(request):
	return render(request, "issue_books.html")