from django.shortcuts import render

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