from django.core.checks import messages
from .models import User, UserManager
from django.shortcuts import render, redirect
from .forms.customForms import LoginForm


import bcrypt
from django.contrib.auth.hashers import make_password

from .forms.user import UserForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        registerForm = UserForm()
        return render(request, 'register.html',  {'registerForm': registerForm})
    else: # "POST"  
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/register')    
        else:
            registerForm = UserForm(request.POST)
            if registerForm.is_valid():
                new_user = registerForm.save()
                print('Nuevo Usuario: ', new_user.name)            
                request.session['logged_userid'] = new_user.id  
                request.session['logged_username'] = new_user.name
            return redirect('/home')                 


def login(request):
    if request.method == "GET":
        loginForm = LoginForm()
        context  = {'loginForm' : loginForm}
        return render(request, 'login.html' ,  context = context)
    else: #POST / autenticacion
        loginForm = LoginForm( request.POST )
        if loginForm.is_valid():
            user = loginForm.login(request.POST)
            if user:
                print("logged user: ", user)
                request.session['logged_userid'] = user.id
                request.session["logged_username"] = user.name
                return redirect('tasks/home')
        return redirect('/login')        



   


def logout(request):
    try: 
        del request.session['logged_username']
        del request.session['logged_userid']
    except:
        print('Error')
    return redirect('/') 

def settings(request):
    return render(request, 'settings.html')           


