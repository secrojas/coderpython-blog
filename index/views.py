from django.shortcuts import render

from posts.models import Post
from categories.models import Category

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

def new_post(request):

    if request.method == 'POST':
        new_post = Post(
            title=request.POST['title'],
            short_description=request.POST['short_description'],
            slug=request.POST['title'],
            status=True
        )
        new_post.save()

        # new_category = Category(title=request.POST['title'],slug=request.POST['title'],description=request.POST['title'],status=True)
        # new_category.save()
        return render(request,'index/home.html',{'new_post':new_post})

    return render(request,'index/new-post.html',{})