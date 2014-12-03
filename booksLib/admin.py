from django.contrib import admin
from booksLib.models import Book

# Register your models here.
#admin.site.register(Book)

#customise the admin form
#order of the fields in a record, fieldsets with title, collapse field
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of Book', {'fields': ['nameB']}),
        ('Date Published', {'fields': ['datePubB'], 'classes': ['collapse']}),
        ('Name of Publisher', {'fields': ['namePubB'], 'classes': ['collapse']}),
        ('Comment',  {'fields': ['commentB'], 'classes': ['collapse']}),
        ('id of Book',  {'fields': ['idB'], 'classes': ['collapse']}),
    ]
admin.site.register(Book,  QuestionAdmin)




