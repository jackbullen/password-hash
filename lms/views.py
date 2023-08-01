from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def home(request):
    return render(request, 'lms/home.html')

def user_registration(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'Username taken')
                return redirect('lms:user_registration')
            else:
                user = User.objects.create_user(username = user_name, password = password1)
                user.save()
                return redirect('lms:login')
        else:
            return redirect('lms:user_registration')
    else:
        return render(request, 'lms/user_registration.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = user_name, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid username and password')
            return redirect('lms:login')
    else:
        return render(request, 'lms/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
    




