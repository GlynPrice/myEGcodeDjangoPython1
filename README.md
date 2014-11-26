myEGcodeDjangoPython1
=====================

My First Python-Django code

This simple example of Django-Python code was developed on a laptop running Ubuntu 14.04 LTS installed alongside MS windows 7. Further, the Python (version 2.7.6) inherent in the Ubuntu system was used. A Python virtual environment was created and the Django software package version 1.7.1 was installed in this virtual environment.

The Django-Python code is based on the tutorial and sample code on the www.docs.djangoproject(polls apps) website and the www.djangobook.com website.

The specifications for this Django-Python code are:
(a) one Model
    i.e one table in the database and one def routine in models.py
(b) no migration after the first migration
(c) few simple views
(d) based on the sqlite3 database (inherent in Python) and the basic web server (inherent in Django)

The view-URLs for this code are:
localhost:8000
localhost:8000/admin
localhost:8000/booksLib/latest
localhost:8000/booksLib/time

Note that the localhost:8000 view-URL is not the Django Welcome view or a crash/error_message, but uses either the view.py in the subfolder for either the Django project or the apps(booksLib) (to swoop need code change).

The localhost:8000/admin view-URL is the Django admin login facility and the other two view-URL uses view.py in the apps(booksLib) subfolder.

