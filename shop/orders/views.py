from django.shortcuts import render
from django.db import transaction

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from settings.base import SHOP_NAME


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                
            cart.clear()
            
            return render(request, 'created_order.html', {'keywords': 'Недорогие товары, быстрая доставка, Минск, sale', 
                                                          'order': order, 
                                                          'shop_name': SHOP_NAME,})
    else:
        form = OrderCreateForm()
    
    return render(request, 'create_order.html', {'title': 'Заказ', 'keywords': 'Недорогие товары, быстрая доставка, Минск, sale',
                                                 'cart': cart, 
                                                 'form': form, 
                                                 'shop_name': SHOP_NAME,})