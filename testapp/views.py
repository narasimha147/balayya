from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time(k):
    date=datetime.datetime.now()
    n='<h1 style="color:red; text-align:center;">hello narasimha good morning</h1><hr style="width:1000px; border-color:red;">'
    n+='<h2 style="color:yellow; text-align:center;">now server time is:'+str(date)+'</h2>'
    return HttpResponse(n)


