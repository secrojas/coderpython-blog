from django.urls import path
from .views import index, about_me, contact, new_category, new_post, new_comment, list_posts

urlpatterns = [
    path('', index, name='index'),
    path('about-me/', about_me, name='about-me'),
    path('contact/', contact, name='contact'),
    path('new-category/', new_category, name='new-category'),
    path('new-post/', new_post, name='new-post'),
    path('new-comment/', new_comment, name='new-comment'),
    path('posts/', list_posts, name='list-posts')
]
