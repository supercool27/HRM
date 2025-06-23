from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
MARITAL_STATUS = [('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')]
EMPLOYMENT_TYPES = [('Full Time', 'Full Time'), ('Intern', 'Intern'), ('Contract', 'Contract')]

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Personal Details
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    
    # Contact Info
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Job Details
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    join_date = models.DateField()
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    # Banking Info
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)

    # System Info
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"
