from django.shortcuts import render
from . import forms

def register(request):
    form_user_register = forms.RegisterUserForm()
    context = {'form_user_register': form_user_register}
    return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'login/register.html.jinja')

def logout(request):
    return render(request, 'logout/register.html.jinja')