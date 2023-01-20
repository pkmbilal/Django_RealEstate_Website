from django.shortcuts import render, redirect
from accounts.forms import RegisterForm

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
