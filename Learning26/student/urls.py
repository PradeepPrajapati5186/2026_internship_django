from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.studenthome),
    path('dashboard/',views.studentDashboard),
    path('login/',views.studentLogin),
    path('servicelist/',views.serviceList, name = 'servicelist'),
    path("createService/",views.createService,name="createService"),
]