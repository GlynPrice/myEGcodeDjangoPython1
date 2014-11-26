from django.contrib import admin
from booksLib.models import Book

# Register your models here.
#admin.site.register(Book)

#customise the admin form
#order of the fields in a record, fieldsets with title, collapse field
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('nameBook',               {'fields': ['nameFld']}),
        ('Date Pub',             {'fields': ['pubDateFld'], 'classes': ['collapse']}),
        ('Pub Name',             {'fields': ['namePubFld'], 'classes': ['collapse']}),
        ('Comment',              {'fields': ['interestingFld'], 'classes': ['collapse']}),
    ]
admin.site.register(Book,  QuestionAdmin)




