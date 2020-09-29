from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm

def register(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
        else:
            form = CreateUserForm()
            
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def user_login_authentication(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('creator')
        else:
            messages.info(request, 'username/password is incorrect')

    context_view = {}
    return render(request, 'accounts/login.html', context_view)

def user_logout(request):
    logout(request)
    return redirect('login')