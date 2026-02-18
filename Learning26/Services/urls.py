from django.urls import path
from . import views
urlpatterns = [
    path("List/",views.ServiceList,name = "list"),
    path("Create/",views.createService, name ='create'),
    path("updateService/<int:id>",views.updateService,name = "update"),
    path("deleteService/<int:id>",views.deleteService,name="delete")
]