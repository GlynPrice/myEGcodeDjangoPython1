#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url

from booksLib import views

#urlpatterns = patterns('',
#    (r'^latest_books/$', views.latest_books),
#)
urlpatterns = patterns('',
   url(r'^latest$', views.latest_books, name='latest_books'),
   url(r'^time$', views.time_books, name='time_books'),
)
print "booksLib/urls.py urlpatterns= ", urlpatterns

