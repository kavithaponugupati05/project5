from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_function(request):
    return HttpResponse('<h1><marquee>this is application</marquee></h1>')
    
