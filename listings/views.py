from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def hello(request):
    return HttpResponse('<h1>Hello django</h1>')

def about(request):
    return HttpResponse('<h1>About django</h1>')

def contact(response):
    return HttpResponse('<h1>Contact</h1>')

def listing(response):
    return HttpResponse('<h1>Listing</h1>')