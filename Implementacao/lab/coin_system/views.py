from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "authentication\index.html")

def signin(request):
    return render(request, "authentication/signin.html") 

def signup(request):
    return render(request, "authentication/signup.html") 

def signout(request):
    pass