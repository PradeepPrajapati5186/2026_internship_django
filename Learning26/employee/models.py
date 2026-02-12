from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    fees = models.IntegerField()
    durationChoice = [(3,"3 months"),(6,"6 months"),(12,"12 months")]
    duration = models.IntegerField(choices = durationChoice , default=3)

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.courseName
class Project(models.Model):
    projectName = models.CharField(max_length =100)
    employeeAssigned = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Completed = models.BooleanField(default=True)
    due_date = models.DateField(default = 'NULL')

    class Meta:
        db_table = "project"
    def __str__(self):
        return self.projectName
class Department(models.Model):
    DeptName = models.CharField(max_length=100)
    location = models.IntegerField(choices=[(0,"Ground Floor"),(1,"First Floor"),(2,"Second Floor")])
    Deptincharge = models.ForeignKey(Employee,on_delete=models.CASCADE)
    class Meta:
        db_table = "department"
    def __str__(self):
        return self.DeptName