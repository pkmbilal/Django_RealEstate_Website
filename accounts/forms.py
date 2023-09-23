from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg'})
        }