from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib import messages

from settings.base import SHOP_NAME
from .forms import LoginForm


def logout_user(request):
    logout(request)
    return redirect(reverse('home_page'))


# def user_login(request): 
#     ctx = {
#             'title': 'Войти',
#             'shop_name': SHOP_NAME,
#           }   
#     return render(request, 'login.html', ctx)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')

                    return redirect('home_page')
                else:
                    messages.success(request, 'Активируйте аккаунт прежде чем войти!')
                    # return HttpResponse('Disabled account')
            else:
                messages.success(request, 'Неверный логин или пароль!')
            #     return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    
    ctx = {
            'title': 'Войти',
            'shop_name': SHOP_NAME,
            'form': form,
          }

    return render(request, 'login.html', ctx)