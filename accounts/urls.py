from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ /accounts/ is working!")

urlpatterns = [
    path('', index),  # Test root
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
