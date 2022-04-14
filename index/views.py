from django.shortcuts import redirect, render

from categories.models import Category
from posts.models import Post
from comments.models import Comment

from .forms import SearchPost

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MyUserForm

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

@login_required
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

#admin views

def my_register(request):
    
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            # return render(request, 'accounts/index.html', {'msj': f'Se crea correctamente al usuario {username}'})
            return redirect('login')
        else:
            return render(request, 'admin/register-page.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = MyUserForm()
    return render(request, 'admin/register-page.html', {'form': form})

def my_login(request):

    msj = ''
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # return render(request, 'index/home.html', {})
                return redirect('content-admin')
            else:
                msj = 'El usuario no se pudo autenticar.'
                # return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': 'El usuario no se pudo autenticar.'})
        else:
            # return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': 'El formulario no es valido.'})
            msj = 'El formulario no es valido.'

    login_form = AuthenticationForm()
    # return render(request,'admin/login-page.html',{'login_form':login_form})
    return render(request, 'admin/login-page.html', {'login_form': login_form, 'msj': msj})

@login_required
def content_admin(request):
    return render(request,'admin/dashboard.html',{})


    