# employee/views.py
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})
