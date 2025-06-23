from django.db import models
from employee.models import Employee

class EmergencyContact(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.relation}"
