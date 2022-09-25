from django.shortcuts import render

def landing(request):
	return render(request, "landing.html")

def addbooks(request):
	return render(request, "books_view.html")

def addmembers(request):
	return render(request, "members_view.html")

def issuebooks(request):
	return render(request, "issue_books.html")