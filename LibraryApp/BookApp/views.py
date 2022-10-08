import json
import datetime
import requests
from .models import Member, Book, Transaction
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def landing(request):
	return render(request, "landing.html")

def addbook(request):
	if request.method == "POST":
		title = request.POST['title'].strip()
		authors = request.POST['authors'].strip()
		isbn = request.POST['isbn'].strip()
		publisher = request.POST['publisher'].strip()
		stock = request.POST['stock'].strip()

		# Checking if any field is blank
		if len(title) == 0 or len(authors) == 0 or len(isbn) == 0 or len(publisher) == 0 or len(stock) == 0:
			messages.error(request, "Don't leave any field blank.")
			return render(request, "add_book.html")
		
		# Checking if stock is a positive number
		if int(stock) < 0:
			messages.error(request, "Stock value should be greater than zero.")
			return render(request, "add_book.html")

		# adding a book in database
		try:
			for i in range(int(stock)):
				Book.objects.create(title=title, authors=authors, isbn=isbn, publisher=publisher)
		except IntegrityError:
			messages.error(request, "Error occured. Please try again")
			return render(request, "add_book.html")

		messages.success(request, "You have successfully added a new book in Book database.")
		return render(request, "add_book.html")
	
	return render(request, "add_book.html")

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
	
	# Getting information from frontend about the books and stocks that needs to be added in db
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
			messages.error(request, "Don't leave any field blank.")
			return render(request, "members_view.html")
		
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

		messages.success(request, "You have successfully added a new member in Member database.")
		return render(request, "members_view.html")
	return render(request, "members_view.html")

def issuebooks(request):
	if request.method == "POST":
		username = request.POST['username'].strip()
		isbn = request.POST['isbn'].strip()

		# Checking if any field is blank
		if len(username) == 0 or len(isbn) == 0:
			messages.error(request, "Don't leave any fields blank.")
			return render(request, "issue_books.html")

		# validating if member exists or not
		try:
			member = Member.objects.get(username=username)
		except:
			messages.error(request, "Member does not exists.")
			return render(request, "issue_books.html")

		# checking if books are available in database to issue 	
		try:
			book = Book.objects.filter(isbn=isbn, member=None)[0]
		except:
			messages.error(request, f"No books with {isbn} number are available in database.")
			return render(request, "issue_books.html")
		
		# checking if members outstanding debt is higher than 500
		debt = 0
		issued_books = member.book_set.all() # getting all the issued books by the member
		for ib in issued_books:
			issue_date = Transaction.objects.filter(member=member, book=ib, action="issue").last().date
			debt += (datetime.date.today() - issue_date).days * 5 # charges per day for a book is 5
			if debt >= 500:
				messages.error(request, 
					f"{username}'s outstanding debt higher than 500. To issue the book please return/re-issue the books that are already issued")
				return render(request, "issue_books.html")

		# assigning this book to the given member
		book.member = member
		book.save()

		# validating if transactions doesn't happen
		try:
			Transaction.objects.create(member=member, book=book, action="issue")
		except IntegrityError:
			messages.error(request, "Transaction did not complete. Try again!")
			return render(request, "issue_books.html")

		messages.success(request, f"{username} issued the book successfully.")

	return render(request, "issue_books.html")

def returnbooks(request):
	if request.method == "POST":
		username = request.POST['username'].strip()
		bookID = request.POST['bookID'].strip()

		# Checking if any field is blank
		if len(username) == 0 or len(bookID) == 0:
			messages.error(request, "Don't leave any fields blank.")
			return render(request, "issue_books.html")

		# validating if member exists or not
		try:
			member = Member.objects.get(username=username)
		except:
			messages.error(request, "Member does not exists.")
			return render(request, "issue_books.html")
		
		# checking if book exists or not and if member has issued this book or not
		try:
			book = Book.objects.get(pk=bookID, member=member)
		except:
			messages.error(request, "Book does not exists. (This can also occur if member has not issued this book)")
			return render(request, "issue_books.html")

		amount = (datetime.date.today() - Transaction.objects.filter(book=book, member=member, action='issue').last().date).days * 5
		if amount < 0:
			messages.success(request, f"{username} returned the book successfully")
		messages.info(request, amount)

		# making the book available to issue again
		book.member = None
		book.save()

		# validating if transactions doesn't happen
		try:
			Transaction.objects.create(member=member, book=book, action="return", fees=amount)
		except IntegrityError:
			messages.error(request, "Transaction did not complete. Try again!")
			return render(request, "issue_books.html")

		# messages.success(request, f"{username} returned the book successfully.")

	return render(request, "issue_books.html")

def books(request):
	if request.method == "POST":
		title = request.POST['title'].strip()
		authors = request.POST['authors'].strip()

		# Checking if any field is blank
		if len(title) == 0 and len(authors) == 0:
			messages.error(request, "Don't leave the fields blank.")
			return render(request, "books.html")

		# storing all the records in books
		try:
			books = Book.objects.filter(title__icontains=title, authors__icontains=authors)
		except IntegrityError:
			messages.error(request, "Internal server error. Try again!")
			return render(request, "books.html")

		# if no books exists in the database for the entered query
		if len(books) == 0:
			messages.warning(request, "Book doesn't exist in the database.")
			return render(request, "books.html")

		return render(request, "books.html", {
			"books" : books
		})

	books = Book.objects.all()
	return render(request, "books.html", {
		"books" : books
	})

def members(request):
	if request.method == "POST":
		first_name = request.POST['first_name'].strip()
		last_name = request.POST['last_name'].strip()
		username = request.POST['username'].strip()

		# Checking if any field is blank
		if len(first_name) == 0 and len(last_name) == 0 and len(username) == 0 and len(email) == 0:
			messages.error(request, "Don't leave the fields blank.")
			return render(request, "members.html")

		# storing all the records in books
		try:
			members = Member.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name, username__icontains=username)
		except IntegrityError:
			messages.error(request, "Internal server error. Try again!")
			return render(request, "members.html")

		# if no books exists in the database for the entered query
		if len(members) == 0:
			messages.warning(request, "Book doesn't exist in the database.")
			return render(request, "members.html")

		return render(request, "members.html", {
			"members" : members
		})

	members = Member.objects.all()
	return render(request, "members.html", {
		"members" : members
	})

def delete(request):
	if request.method == "POST":
		book = json.load(request)
		bookid = book['data'].split('\t')[0]
		res = Book.objects.get(pk=bookid)
		res.delete()
	return HttpResponseRedirect(reverse("books"))