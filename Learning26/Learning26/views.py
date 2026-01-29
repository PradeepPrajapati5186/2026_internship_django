from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def aboutUs(request):
    return render(request,"Aboutus.html")
def contactUs(request):
    return render(request,"contactus.html")
def recipe(request):
    ingrediants =['Tomato','Masala','Noodles']
    data={'name':"Maggie",'ingrediants':ingrediants, 'Time':2}

    return render(request,"recipe.html",data)
def team(request):
    CSK = ['Ruturaj Gaikwad','Ayush Mhatre','Sanju Samson','Venkatesh Iyer','Dewald Brevis','Shivam Dube','Jamie Overton','MS Dhoni','Anshul Kamboj','Khaleel Ahmed','Nathan Ellis','Noor Ahmad']
    data = {'teamName':'CSK','Squad': CSK,'Captain':CSK[7],'trophies':5}
    return render(request,"Team.html",data)
def player(request):
    teams = ["Argentina","Barcelona",'PSG','Inter Miami CIty']
    data = {'playername':'Messi','teamsplayed': teams,"ballonDor":8}
    return render(request,'player.html',data)