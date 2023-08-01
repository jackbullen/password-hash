from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'lms'

urlpatterns = [
    path('', home, name="home"),
    path('user_registration', user_registration, name='user_registration'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]