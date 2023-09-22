from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password

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
    
# Change Password
@login_required
def ChangePassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')

        if not username or not current_password or not new_password:
            print('Username or Current password or New password field is empty!!!')
            return render(request,'registration/change_password.html')

        # Check Current Password is Mathing or Not
        try:
            user = User.objects.get(username=username)
            if not user.check_password(current_password):
                print('Wrong Current Password!!!')
                return render(request,'registration/change_password.html')
        except User.DoesNotExist:
            print('User not exist!!!')
            return render(request,'registration/change_password.html')
        
        # Check New Password is valid or not
        try:
            validate_password(new_password)
        except Exception:
            print('Password is not valid!!!')
            return render(request,'registration/change_password.html')
        user.set_password(new_password)
        user.save()
        return redirect('login')
    else:
        return render(request,'registration/change_password.html')
