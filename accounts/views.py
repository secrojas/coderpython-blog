from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MyUserForm


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
def content_admin(request):
    return render(request,'accounts/dashboard.html',{})
