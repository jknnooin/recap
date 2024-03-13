from django.shortcuts import render, HttpResponse
from .models import loginModel

# Create your views here.

def home(request):
    #return HttpResponse("hello world!")
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    creds =  loginModel.objects.all()
    return render(request, "profile.html", {"credentials": creds})