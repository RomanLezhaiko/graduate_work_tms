from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('signup/', views.signup, name='register_user'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'), 
]