from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(req):
    return render(req, "index.html")
