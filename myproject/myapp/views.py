from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
   
    return render(request, 'myapp/index.html')

def about(request):
   
    return render(request, 'myapp/about.html')

def contact(request):
   
    return render(request, 'myapp/contact.html')


def donate(request):
   
    return render(request, 'myapp/donate.html')



def error(request):
   
    return render(request, 'myapp/error.html')



def myservice(request):
   
    return render(request, 'myapp/myservice.html')


def portfolio(request):
   
    return render(request, 'myapp/portfolio.html')


