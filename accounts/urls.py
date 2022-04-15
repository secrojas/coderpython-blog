from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import content_admin,my_login,my_register

urlpatterns = [
    # admin routes
    path('content-admin/', content_admin, name='content-admin'),
    path('login/', my_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='index/home.html'), name='logout'),
    path('register/', my_register, name='register')   
    
]