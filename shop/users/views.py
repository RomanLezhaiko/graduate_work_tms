from django.shortcuts import render
from settings.base import SHOP_NAME


def user_login(request): 
    ctx = {
            'title': 'Войти',
            'shop_name': SHOP_NAME,
          }   
    return render(request, 'login.html', ctx)