from django.shortcuts import render, redirect
from . import forms

def register(request):
    if request.method == 'POST':
        form_user_register = forms.RegisterUserForm(request.POST)
        if form_user_register.is_valid():
            form_user_register.save()
            return redirect('login')
        else:
            print(form_user_register.error_messages)
    form_user_register = forms.RegisterUserForm()
    context = {'form_user_register': form_user_register}
    return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'login/register.html.jinja')

def logout(request):
    return render(request, 'logout/register.html.jinja')