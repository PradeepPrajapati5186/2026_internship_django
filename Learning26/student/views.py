from django.shortcuts import render

def studenthome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    student = {'name':'pradeep','marks':93,'city':'Ahemdabad'}
    return render(request,"student/studentDashboard.html",student)

def studentLogin(request):
    return render(request,"student/studentLogin.html")
