from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/',views.loginView,name='login'),
    path('forgot_password/',views.ForgotPassword,name='forgot_password'),
    path('change_password/',views.ChangePassword,name='change_password')
]