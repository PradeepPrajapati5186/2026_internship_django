from django.urls import path
from . import views
urlpatterns = [
    path("empdashboard/",views.employeeDashboard),
    path('filter/',views.employeefilter),
]