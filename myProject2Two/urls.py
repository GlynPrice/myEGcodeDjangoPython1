from django.conf.urls import patterns, include, url
from django.contrib import admin


#match url of the type localhost:8000
#a8000 = url(r'^$', 'booksLib.views.xxxx')
#print "a8000= ", a8000

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myProject2Two.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #match url of the type localhost:8000
    #folder module  def-routine
    #either of following would work
    #url(r'^$', 'myProject2Two.views.xxxx'),
    url(r'^$', 'booksLib.views.xxxx'),

    #match url of the type localhost:8000/booksLib/latest
    #url(r'^booksLib/', include('booksLib.urls')),
    #match url of the type localhost:8000/booksLib/time
    #url(r'^booksLib/', include('booksLib.urls')),
    #Namespacing URL name
    url(r'^booksLib/', include('booksLib.urls', namespace="booksLib")),
    #match url of the type localhost:8000/admin
    url(r'^admin/', include(admin.site.urls)),
)
print "myProject2Two/urls.py urlpatterns= ", urlpatterns

#url of the type localhost:8000      (root, home location)
#Only get the 'Welcome to Django, It Worked, Congratulations...'
#if the urlpatterns is empty or has only admin stuff in it.
#In the code above can captured this type of url, but
#cannot send it to the 'Welcome to Django....' view, but
#can send it to either of two xxxx view created in this project/app


#a1= include(admin.site.urls)
#print "a1= ", a1
#a2= url(r'^admin/', include(admin.site.urls))
#print "a2= ", a2

#b1= include('booksLib.urls')
#print "b1= ", b1
#b2= url(r'^latest/', include('booksLib.urls'))
#print "b2= ", b2


