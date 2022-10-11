# BookApp - A Library Management Web Application

## About

BookApp is a library management web appliction for librarian's. This app is built as a part of [hiring test](https://frappe.io/dev-hiring-test) for [Frappe](https://frappe.io/). The backend for this app is built in Django (A Python web framework) and Bootstrap (A Responsive CSS framework) is used for frontend.


## Setup and Installation

1. Clone the Repo
```sh
git clone https://github.com/MotilalChavhan/BookApp.git
```
2. Install Requirements
At first, Go to the project directory.
```sh
cd BookApp/LibraryApp
```
Then install the requirements by using following command.
```sh
python install -r requirements.txt
```

3. Setup .env file
```sh
echo "secret_key=django-insecure-*rgr77#56w&j)fi2in0)+6171ud$89%%4q0&%)ifdwg9vp042m" > .env
```

4. Migrate and Run
Migrate the database schema using following command.
```sh
python manage.py migrate
```
Now, run the app using the following command.
```sh
python manage.py runserver
```
Go to 127.0.0.1:8000 on your browser.

## Overview

Landing page

![landing page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/landing.gif)

Import Books via [frappe API](https://frappe.io/api/method/frappe-library)

![import books](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/importBooks.gif)

Add Book page

![add book page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/addbook.gif)

Add Member page

![add member page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/addmember.gif)

Issue/Return page

![issue/return page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/issueReturn.gif)

Outstanding Debt Example

![outstanding debt example](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/outstandingDebt.gif)

Books page (search, delete, edit)

![books page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/books.gif)

Members page (search, delete, edit)

![members page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/members.gif)

Transactions page

![transactions page](https://raw.githubusercontent.com/MotilalChavhan/BookApp/main/gifs/transactions.gif)