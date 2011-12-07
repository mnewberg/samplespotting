from django.utils import simplejson
from dajaxice.core import dajaxice_functions
import views

def myexample(request):
    return search(request)

dajaxice_functions.register(myexample)
