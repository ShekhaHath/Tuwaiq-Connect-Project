from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_page(request : HttpRequest):
    return render (request,"main/home_page.html")