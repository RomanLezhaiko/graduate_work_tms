from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from settings import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'shop.views.handler404'
handler500 = 'shop.views.handler500'