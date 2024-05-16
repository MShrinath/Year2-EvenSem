from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage,name='homePage'),
    path('login', views.LoginPage,name='loginPage'),
    path('signup', views.SignupPage,name='signupPage'),
    path('ls', views.ls,name='ls'),
    path('lf', views.lf,name='lf'),
    path('signupuser', views.SignupUser,name='signupUser'),
    path('loginuser', views.LoginUser,name='loginUser'),
]