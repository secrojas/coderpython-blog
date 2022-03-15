from django.urls import path
from .views import index, about_me, posts, contact

urlpatterns = [
    path('', index, name='index'),
    path('about-me/', about_me, name='about-me'),
    path('posts/', posts, name='posts'),
    path('contact/', contact, name='contact')
]
