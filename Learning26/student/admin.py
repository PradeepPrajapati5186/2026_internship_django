from django.contrib import admin
from .models import student,StudentProfile,Service,Category

admin.site.register(student)
admin.site.register(StudentProfile)
admin.site.register(Service)
admin.site.register(Category)
# Register your models here.
