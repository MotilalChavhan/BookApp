import json
import requests
from .models import Member, Book
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def landing(request):
	return render(request, "landing.html")

def getbooks(request):
	if request.method == "GET":
		return render(request, "books_view.html")

	# Fetching the books details from frappe API 

	url = "https://frappe.io/api/method/frappe-library"
	payload = {
		"title" : request.POST['title'],
		"authors" : request.POST['authors'],
		"isbn" : request.POST['isbn'],
		"publisher" : request.POST['publisher'],
		"page" : request.POST['page']
	}
	response = requests.request("POST", url, json=payload)
	
	# Checking if the response from frappe API returns book details if not, it renders a blank books_view page
	try:
		data = response.json()["message"]
	except:
		return render(request, "books_view.html")
	

	return render(request, "books_view.html", {
		"books" : data
	})

def addbooks(request):
	if request.method == 'GET':
		return HttpResponseRedirect(reverse("getbooks"))
	
	# Getting information from frontend about the books and stocks thats needed to add in db
	data = json.load(request)
	books = data["books"]
	stocks = data["stocks"] # No. of books to enter with same book details

	# Returning status fail if stocks is empty list
	if len(stocks) == 0:
		return JsonResponse({"status" : "fail", "message" : "Please enter the no. of books to add into database in stocks field provided"})
	
	# Making sure if adding books to database is working fine if not returns a json with status fail. 
	try:
		for i in range(len(books)):
			book = books[i].split('\t')
			for j in range(int(stocks[i])):
				Book.objects.create(title=book[0], authors=book[1], isbn=book[2], publisher=book[3])
		return JsonResponse({"status" : "success", "message" : "You have successfully added the books in your database."})
	except:
		return JsonResponse({"status" : "fail", "message" : "Internal Server Error"})

def addmembers(request):
	if request.method == "POST":
		first_name = request.POST['first_name'].strip()
		last_name = request.POST['last_name'].strip()
		username = request.POST['username'].strip()
		email = request.POST['email'].strip()

		# Checking if any field is blank
		if len(first_name) == 0 or len(last_name) == 0 or len(username) == 0 or len(email) == 0:
			return render(request, "members_view.html", {
				"status" : "fail",
				"message" : "Don't leave any field blank."
			})
		
		# Validating email
		try:
			validate_email(email)
		except ValidationError:
			messages.error(request, "Enter a valid email.")
			return render(request, "members_view.html")

		# adding a member in database
		try:
			Member.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
		except IntegrityError:
			messages.error(request, "username/email already exists. Enter a different username/email.")
			return render(request, "members_view.html")

		messages.success(request, "You have successfully added a new member in your database.")
		return render(request, "members_view.html")
	return render(request, "members_view.html")

def issuebooks(request):
	return render(request, "issue_books.html")