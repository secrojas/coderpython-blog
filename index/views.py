from django.shortcuts import redirect, render
from categories.models import Category
from posts.models import Post
from comments.models import Comment
from .forms import SearchPost
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


def index(request):    
    posts = Post.objects.all()    
    return render(request,'index/home.html',{'posts':posts})

def about_me(request):   

    datos = {
        'lista' : ['primero','segundo','tercero'],
        'nombre' : 'Juancho'
    }

    return render(request, 'index/about-me.html', datos)

def posts(request):
    return render(request,'index/posts.html',{})

def contact(request):
    return render(request,'index/contact.html',{})

@login_required
def new_category(request):

    if request.method == 'POST':
        new_category = Category(
            title=request.POST['title'],
            slug=request.POST['title'],
            description=request.POST['description'],
            status=True
        )
        new_category.save()

        return redirect('index')

    return render(request,'index/new-category.html',{})

@login_required
def new_post(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        new_post = Post(
            title=request.POST['title'],
            short_description=request.POST['short_description'],
            slug=request.POST['title'],
            status=True,
            category=Category.objects.get(id=request.POST['category'])
        )
        new_post.save()

        return redirect('index')

    return render(request,'index/new-post.html',{'categories':categories})

@login_required
def new_comment(request):

    if request.method == 'POST':
        new_comment = Comment(
           content = request.POST['content']
        )
        new_comment.save()

        return redirect('index')

    return render(request,'index/new-comment.html',{})

def list_posts(request):

    post_to_find = request.GET.get('title',None)

    if post_to_find is not None:
        posts = Post.objects.filter(title__icontains = post_to_find)
    else:
        posts = Post.objects.all()

    form = SearchPost()

    return render(request, 'index/posts.html',{'form':form, 'posts':posts})

@login_required
def category_create(request):

    if request.method == 'POST':
        new_category = Category(
            title=request.POST['title'],
            slug=request.POST['title'],
            description=request.POST['description'],
            status=True
        )
        new_category.save()

        return redirect('admin-categories')

    return render(request,'accounts/categories/categories-create.html',{})

class categoriesDetail(DetailView):
    model = Category
    template_name = "accounts/categories/categories-detail.html"
class categoriesEdit(UpdateView):
    model = Category
    template_name = "accounts/categories/categories-edit.html"
    success_url = '/admin/categories'
    fields = ['title', 'description', 'status']  
class categoriesDelete(DeleteView):
    model = Category
    template_name = "accounts/categories/categories-delete.html"
    success_url = '/admin/categories'

@login_required
def post_create(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        new_post = Post(
            title=request.POST['title'],
            short_description=request.POST['short_description'],
            slug=request.POST['title'],
            status=True,
            category=Category.objects.get(id=request.POST['category'])
        )
        new_post.save()

        return redirect('admin-posts')

    return render(request,'accounts/posts/posts-create.html',{'categories':categories})

class postsDetail(DetailView):
    model = Post
    template_name = "accounts/posts/posts-detail.html"
class postsEdit(UpdateView):
    model = Post
    template_name = "accounts/posts/posts-edit.html"
    success_url = '/admin/posts'
    fields = ['title', 'short_description', 'status']  
class postsDelete(DeleteView):
    model = Post
    template_name = "accounts/posts/posts-delete.html"
    success_url = '/admin/posts'
