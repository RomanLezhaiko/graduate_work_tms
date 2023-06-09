from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from settings.base import SHOP_NAME



@require_POST
def update_cart(request):
    cart = Cart(request)
    if len(cart) > 0:
        tmp_dict = dict(request.POST)
        product_id_list = tmp_dict['product_id']
        quantity_list = tmp_dict['quantity']
        products = list(Product.objects.filter(id__in=product_id_list))
        
        for i in range(len(products)):
            cart.add(product=products[i], quantity=int(quantity_list[i]), update_quantity=int(quantity_list[i]))

        return redirect('order_create')
    
    messages.success(request, 'Ваша корзина пуста. Добавьте хотя бы один товар.')
    return redirect('cart_detail')


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    messages.success(request, "Товар добавлен в корзину.")

    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'title': 'Корзина', 
                                                'keywords': 'Недорогие товары, быстрая доставка, Минск, sale',
                                                'cart': cart, 
                                                'shop_name': SHOP_NAME,})