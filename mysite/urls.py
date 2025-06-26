from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),


    path('', TemplateView.as_view(template_name='accounts/login.html')),
]