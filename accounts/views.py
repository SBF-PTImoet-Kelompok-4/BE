from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
import os
from test_project.settings import BASE_DIR

def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.username == 'admin_username':  
                user.is_staff = True  
                user.is_superuser = True  
                user.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('accounts:login')
        

    template_path = os.path.join(BASE_DIR, 'accounts', 'templates', 'accounts', 'register.html')
    return render(request, template_path, {'form': form})

def login_user(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('crud:index')
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('accounts:login')