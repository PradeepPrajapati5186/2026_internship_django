from django.urls import path
from . import views
urlpatterns = [
    path("empdashboard/",views.employeeDashboard),
    path('filter/',views.employeefilter),
    path('create/',views.createEmployeewithform),
    path('createCourse/',views.createCoursewithform),
    path('createProject/',views.createProjectwithform),
    path('createDepartment/',views.createDepartmentwithform)
]