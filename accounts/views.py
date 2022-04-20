from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MyUserForm, EditFullUser
from .models import MyUser

from categories.models import Category
from posts.models import Post

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
            return render(request, 'accounts/register-page.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = MyUserForm()
    return render(request, 'accounts/register-page.html', {'form': form})

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
    return render(request, 'accounts/login-page.html', {'login_form': login_form, 'msj': msj})

@login_required
def edit_user(request):
    
    user_extension_logued, _ = MyUser.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditFullUser(request.POST, request.FILES)
        
        if form.is_valid():
            
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('index')
        else:
            return render(request, 'accounts/profile.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = EditFullUser(
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def content_admin(request):
    return render(request,'accounts/dashboard.html',{})

@login_required
def profile(request):
    more_data, _ = MyUser.objects.get_or_create(user=request.user)
    return render(request,'accounts/profile.html',{'more_data':more_data})

@login_required
def admin_categories(request):
    categories = Category.objects.all()
    return render(request,'accounts/categories/categories.html',{'categories':categories})

@login_required
def admin_posts(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request,'accounts/posts/posts.html',{'categories':categories,'posts':posts})

