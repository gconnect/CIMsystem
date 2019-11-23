from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from django.http import HttpResponse
# Create your views here.
def index (request):
   return  render(request, 'cisystem/index.html')

def about (request):
   return  render(request, 'cisystem/about.html')

def login (request):
   return  render(request, 'cisystem/login.html')

def contact(request):
   return render(request, 'cisystem/contact.html')

