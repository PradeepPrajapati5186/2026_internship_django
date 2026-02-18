from django.shortcuts import render,HttpResponse,redirect
from . models import Service
from . forms import ServiceForm

def ServiceList(request):
    Services = Service.objects.all().values()
    return render(request,'Services/ServiceList.html',{'service':Services})



def createService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        form.save()
        return HttpResponse("Service Created")
    else:
        form = ServiceForm()
        return render(request,'Services/ServiceForm.html',{'form':form})
    
def deleteService(request,id):
    print("id from url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("list")

def updateService(request,id):
    service = Service.objects.get(id=id)
    
    if request.method == "POST":
        form = ServiceForm(request.POST,instance=service)
        form.save()
        return redirect("list")
    else:
        form = ServiceForm(instance=service)    
        return render(request,"Services/updateService.html",{"form":form})