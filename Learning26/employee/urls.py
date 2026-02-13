from django.urls import path
from . import views
urlpatterns = [
    path("empdashboard/",views.employeeDashboard,name ="employeeList"),
    path('filter/',views.employeefilter),
    path('create/',views.createEmployeewithform,name="createEmployeeWithForm"),
    path('createCourse/',views.createCoursewithform),
    path('createProject/',views.createProjectwithform),
    path('createDepartment/',views.createDepartmentwithform),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("sortEmployee/<int:id>",views.sortEmployee,name="sortEmployee")
]