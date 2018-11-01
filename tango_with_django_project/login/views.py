from django.shortcuts import render, redirect, reverse
from login.models import User
from login.forms import LoginForm


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        message = "所有字段都必须填写"
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect(reverse('user:index'))
                else:
                    message = "password error"
            except:
                message = "user is no exit"
        return render(request, 'login/login.html', locals())
    form = LoginForm()
    return render(request, 'login/login.html', locals())


def register(request):
    return render(request, 'login/register.html')


def logout(request):
    return redirect('/index.html')
