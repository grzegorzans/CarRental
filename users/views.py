from django.shortcuts import render
from . import forms

def register(request):
    if request.method == 'POST':
        form_user_register = forms.RegisterUserForm(request.POST)
        if form_user_register.is_valid():
            form_user_register.save()
            context = {'message': 'Success!'}
        else:
            pas1 = form_user_register.cleaned_data.get("password1")
            pas2 = form_user_register.cleaned_data.get("password2")
            if pas1==pas2:
                print("Zgodne")
            print(pas1)
            print(pas2)
            print(form_user_register.error_messages)
            context = {'message': 'Zonk!'}
        return render(request, 'users/register.html.jinja', context=context)
    else:
        form_user_register = forms.RegisterUserForm()
        context = {'form_user_register': form_user_register}
        return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'login/register.html.jinja')

def logout(request):
    return render(request, 'logout/register.html.jinja')