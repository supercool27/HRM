# employee/urls.py
from django.urls import include, path
from .views import employee_list

urlpatterns = [
    path('', employee_list, name='employee-list'),
]

# project/urls.py
path('employees/', include('employee.urls')),
