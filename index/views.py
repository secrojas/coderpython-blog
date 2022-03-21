from django.shortcuts import redirect, render

from categories.models import Category
from posts.models import Post
from comments.models import Comment

from .forms import SearchPost

def index(request):
    return render(request,'index/home.html',{})

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

def new_category(request):

    if request.method == 'POST':
        new_category = Category(
            title=request.POST['title'],
            slug=request.POST['title'],
            description=request.POST['title'],
            status=True
        )
        new_category.save()

        return redirect('index')

    return render(request,'index/new-category.html',{})

def new_post(request):

    if request.method == 'POST':
        new_post = Post(
            title=request.POST['title'],
            short_description=request.POST['short_description'],
            slug=request.POST['title'],
            status=True,
            # category=request.POST['category'],
        )
        new_post.save()

        return redirect('index')

    return render(request,'index/new-post.html',{})

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
    