from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime
from booksLib.models import Book

# Create your views here.

def xxxx(request):
    print "xxxx(request): A"
    return HttpResponse("You're at: url=localhost:8000/, app= booksLib(booksLib), def-view= xxxx")

def time_books(request):
    tNow = datetime.datetime.now()
    htmlMY = "<html><body>It is now %s.</body></html>" % tNow
    return HttpResponse(htmlMY)

#place-holder code
#def latest_books(request):
#    return HttpResponse("You're at: url= latest, app= booksLib, def-view=latest_books")

#Simple view of data from the database with the page's design (look,
#data arrangement) hard-code in this routine)
#def latest_books(request):
#    latest_book_list = Book.objects.order_by('-pubDateFld')[:5]
#    print "latest_book_list: ", latest_book_list
#
#    output = ';  '.join([p.nameFld for p in latest_book_list])
#    print "output= ", output
#    return HttpResponse(output)

#Simple view of data from the database with the page's design (look,
#data arrangement) separated to a template
#def latest_books(request):
#    latest_book_list = Book.objects.order_by('-pubDateFld')[:5]
#    print "latest_book_list: ", latest_book_list
#
#    template = loader.get_template('booksLib/latest_list.html')
#    context = RequestContext(request, {
#        'latest_book_list': latest_book_list,
#    })
#    return HttpResponse(template.render(context))

#A shortcut that loads a template, fills a context and returns a HttpResponse
#object with the rendered template (common idiom)
def latest_books(request):
    latest_book_list = Book.objects.all().order_by('-datePubB')[:6]
    num_polls1 = len(latest_book_list)                             #ggp1Dec2014
    num_polls2 = len(latest_book_list.all())                       #ggp1Dec2014
    num_polls3 = len(Book.objects.all())                           #ggp1Dec2014
    print 'num_polls1= ', num_polls1, 'num_polls2= ', num_polls2, 'num_polls3= ', num_polls3   #ggp1Dec2014
    #assert False, num_polls1                                                                   #ggp1Dec2014

    print "latest_book_list: ", latest_book_list
    print "latest_books(request): 001"
#   context = {'latest_book_list': latest_book_list}                                                      #ggp1Dec2014
    context = {'latest_book_list': latest_book_list, 'num_polls1': num_polls1, 'num_polls3': num_polls3}  #ggp1Dec2014
    print "latest_books(request): 002"
    print "Book.objects.all()= ", Book.objects.all()  #ggp1Dec2014
    return render(request, 'booksLib/latest_list.html', context)

