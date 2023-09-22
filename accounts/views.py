from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# New User
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

# SignIn
def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user)
            return render(request, 'registration/login.html')
        else:
            return render(request, 'registration/login.html')
    except User.DoesNotExist:
        return render(request, 'registration/login.html')

# Reset Password    
def ForgotPassword(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            if user:
                user.check_password(password)
                user.set_password(password)
                user.save()
                return redirect('login')
        except User.DoesNotExist:
            return render(request,'registration/forgot_password.html')

    else:
        return render(request,'registration/forgot_password.html')
