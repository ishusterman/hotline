#from django.utils import simplejson
from dajaxice.core import dajaxice_functions
import simplejson

def primer(request,message):
    return_message=u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps({'message':return_message})