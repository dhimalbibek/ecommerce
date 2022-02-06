from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from tkinter.messagebox import NO
from django.shortcuts import render
from login.forms import loginform
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_page(request):
    context ={}

    form =loginform(request.POST or None)

    context['form'] = form
    if form.is_valid():
        username =form.cleaned_data.get('username')
        password =form.cleaned_data.get('password')

        user = authenticate(request=request,username=username,password=password)

        if user:
            login(request,user)
        else:
            context['msg'] = 'invalid password'

        return render(request, 'create.html', context)

def logout_page(request):
    logout(request)