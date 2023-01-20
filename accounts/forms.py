from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


# class CustomLoginForm(AuthenticationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

# Registration Form Styling
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')