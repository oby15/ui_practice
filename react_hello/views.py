from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return render(request, "react_hello/index.html")

def counter(request):
    return render(request, "react_hello/counter.html")

def addition(request):
    return render(request, "react_hello/addition.html")