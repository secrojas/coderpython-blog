from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, about_me, contact, new_category, new_post, new_comment, list_posts,content_admin,my_login,my_register

urlpatterns = [
    path('', index, name='index'),
    path('about-me/', about_me, name='about-me'),
    path('contact/', contact, name='contact'),
    path('new-category/', new_category, name='new-category'),
    path('new-post/', new_post, name='new-post'),
    path('new-comment/', new_comment, name='new-comment'),
    path('posts/', list_posts, name='list-posts'),

    path('login/', my_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='index/home.html'), name='logout'),
    path('register/', my_register, name='register'),
    
    # admin routes
    path('content-admin/', content_admin, name='content-admin')
]
