from django.urls import path
from .views import index, about_me, contact, new_category, new_post, new_comment, list_posts,category_create, post_create
from accounts.views import content_admin,admin_categories,admin_posts

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('about-me/', about_me, name='about-me'),
    path('contact/', contact, name='contact'),
    path('new-category/', new_category, name='new-category'),
    path('new-post/', new_post, name='new-post'),
    path('new-comment/', new_comment, name='new-comment'),
    path('posts/', list_posts, name='list-posts'),

    #admin routes
    path('admin/dashboard', content_admin, name='content-admin'),

        #categories
    path('admin/categories', admin_categories, name='admin-categories'),
    path('admin/categories/create', category_create, name='category-create'),
    path('admin/categories/<int:pk>', views.categoriesDetail.as_view(), name='categories-detail'),
    path('admin/categories/<int:pk>/edit', views.categoriesEdit.as_view(), name='categories-edit'),
    path('admin/categories/<int:pk>/delete', views.categoriesDelete.as_view(), name='categories-delete'),

         #posts
    path('admin/posts', admin_posts, name='admin-posts'),
    path('admin/posts/create', post_create, name='posts-create'),
    path('admin/posts/<int:pk>', views.postsDetail.as_view(), name='posts-detail'),
    path('admin/posts/<int:pk>/edit', views.postsEdit.as_view(), name='posts-edit'),
    path('admin/posts/<int:pk>/delete', views.postsDelete.as_view(), name='posts-delete'),
]
