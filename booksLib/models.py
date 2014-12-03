from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    #define fields for this model/table
    nameB = models.CharField(max_length=50)
    datePubB = models.DateField()
    namePubB = models.CharField(max_length=50)
    commentB = models.CharField(max_length=50)
    idB = models.CharField(max_length=50)
    def __unicode__(self):                # __unicode__ on Python 2.7
        #sensible representation of the class/object
        return self.nameB
    def pubDateDiffBol(self):
        #demonstration of a custom method
        tDelta = datetime.timedelta(days=1)
        tNow = timezone.now()
        print "tNow= ", tNow
        print "tDelta= ", tDelta
        myDateDiff= tNow - tDelta
        print "myDateDiff= ", myDateDiff
        #myDateBol = (self.pubDateFld >= tNow - tDelta)
        print "self.pubDateFld= ", self.pubDateFld
        myDateBol = True
        return myDateBol
    #demonstration of few attributes
    pubDateDiffBol.data = 1833
    pubDateDiffBol.boolean = True
    pubDateDiffBol.comment = 'okay'
    def recommended(self):
        #demonstration of a custom method
        if self.interestingFld == "Yes" or self.interestingFld == "yes" or self.interestingFld == "YES":
           myAns = "recommended"
        else:
           myAns = "not recommended"
        return myAns
