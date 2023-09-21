from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def register(request):
    form=RegisterForm()
    context = {'form': form}
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    return render(request, 'register.html', context)

def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user)
            return render(request, 'register/login.html')
    except User.DoesNotExist:
        return render(request, 'register/login.html')
