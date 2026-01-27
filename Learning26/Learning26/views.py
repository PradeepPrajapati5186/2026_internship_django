from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def aboutUs(request):
    return render(request,"Aboutus.html")
def contactUs(request):
    return render(request,"contactus.html")