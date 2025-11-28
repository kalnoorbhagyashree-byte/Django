from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World")
def about(request):
    return HttpResponse("About page")
def welcome (request):
    return render(request,"index.html")
def contact(request):
    return render (request,"contact.html")
# Create your views here.
