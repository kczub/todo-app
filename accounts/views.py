from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm

from accounts.forms import RegistrationForm


def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect(reverse('accounts:login'))
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password.'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        print(request, user)

        return redirect(reverse('todo:profile'))
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('todo:index'))
    return render(request, 'accounts/logout.html', {})
