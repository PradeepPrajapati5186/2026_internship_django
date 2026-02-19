from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm

def studenthome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    student = {'name':'pradeep','marks':93,'city':'Ahemdabad'}
    return render(request,"student/studentDashboard.html",student)

def studentLogin(request):
    return render(request,"student/studentLogin.html")

def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/servicelist.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
        else:
            return render(request,"student/createservice.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createservice.html",{"form":form})
