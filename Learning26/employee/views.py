from django.shortcuts import render,HttpResponse,redirect
from . models import Employee
from . forms import EmployeeForm,CourseForm,DepartmentForm,ProjectForm

def employeeDashboard(request):
    employees = Employee.objects.all().values()
    print(employees)
    return render(request,'employee/employeedashboard.html',{'employee':employees})


def employeefilter(request):
   
    employee = Employee.objects.filter(name ="raj").values()   
    employee2 = Employee.objects.filter(post ="Developer").values()   
    employee3 = Employee.objects.filter(name ="raja",post ="Developer").values()
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

 
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()    

    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

    employee16 = Employee.objects.order_by("age").values()     
    employee17 = Employee.objects.order_by("-age").values()  

    employee18 = Employee.objects.order_by("-salary").values()    

    

 
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    return render(request,'employee/employeefilter.html')

def createEmployeewithform(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        return HttpResponse("Employee created")
    else:
        form = EmployeeForm()
        return render(request,'employee/createEmployeewithform.html',{'form':form})
    
def createCoursewithform(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("Course created")
    else:
        form = CourseForm()
        return render(request,'employee/createCoursewithform.html',{'form':form})
    
def createProjectwithform(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form.save()
        return HttpResponse("Project created")
    else:
        form = ProjectForm()
        return render(request,'employee/createProjectwithform.html',{'form':form})

def createDepartmentwithform(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        form.save()
        return HttpResponse("Department created")
    else:
        form = DepartmentForm()
        return render(request,'employee/createDepartmentwithform.html',{'form':form})
    
def deleteEmployee(request,id):
    print("id from url = ",id)
    Employee.objects.filter(id=id).delete()
    return redirect("employeeList") #url --> name -->


def filterEmployee(request):
    print("filter employee called...")
    employee = Employee.objects.filter(age__gte=20).values()
    print("filter employees = ",employee)
    return render(request,"employee/employeedashboard.html",{"employee":employee})

def sortEmployee(request,id):
    if id == 1:
        employee = Employee.objects.order_by("age").values()
        return render(request,"employee/employeedashboard.html",{"employee":employee})
    elif id ==2:
        employee = Employee.objects.order_by("-age").values()
        return render(request,"employee/employeedashboard.html",{"employee":employee})