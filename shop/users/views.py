from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string 
from django.contrib.auth import get_user_model

from settings.base import SHOP_NAME
from .forms import LoginForm, SignupForm
from .tokens import account_activation_token  
from .tasks import send_email_task
from .models import CustomUser


def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email') 

            send_email_task.delay(mail_subject, message, to_email)
            
            return render(request, 'complete_registration.html', {'title': 'Подтвердите почту', 'shop_name': SHOP_NAME,})
    else:  
        form = SignupForm()  
    
    return render(request, 'signup.html', {'title': 'Регистрация', 'shop_name': SHOP_NAME, 'form': form})  


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save() 

        return render(request, 'account_active.html', {'title': 'Аккаунт активирован', 'shop_name': SHOP_NAME,})
    else:  
        return render(request, 'invalid_token.html', {'title': 'Токен не действителен', 'shop_name': SHOP_NAME,})


def logout_user(request):
    logout(request)
    return redirect(reverse('home_page'))


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')

                    return redirect('home_page')
                else:
                    return render(request, 'complete_registration.html', {'title': 'Подтвердите почту', 'shop_name': SHOP_NAME,})
            else:
                messages.success(request, 'Неверный логин или пароль!')
    else:
        form = LoginForm()
    
    ctx = {
            'title': 'Войти',
            'shop_name': SHOP_NAME,
            'form': form,
          }

    return render(request, 'login.html', ctx)