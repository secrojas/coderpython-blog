from django.urls import path
from .views import index, about_me, posts, contact, new_post

urlpatterns = [
    path('', index, name='index'),
    path('about-me/', about_me, name='about-me'),
    path('posts/', posts, name='posts'),
    path('contact/', contact, name='contact'),
    path('new-post/', new_post, name='new-post')
]
