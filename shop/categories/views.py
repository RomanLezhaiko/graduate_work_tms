from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from categories.models import Category
from settings.base import SHOP_NAME


def get_category_page(request):
    category_all = Category.objects.all()
    ctx = {
        'title': 'Категории',
        'keywords': 'Недорогие товары, быстрая доставка, Минск, sale',
        'shop_name': SHOP_NAME,
        'categories': list(category_all),
    }
    return render(request, 'category_list.html', ctx)


def get_category_by_slug(request, category_slug: str):
    category_all = Category.objects.all()
    category_detail = Category.objects.get(slug=category_slug)
    categories = category_detail.get_descendants(include_self=True)

    queryset_list = []
    for category in categories:
        if category.products.exists():
            queryset_list.append(category.products.all())

    products_list = []
    for qs in queryset_list:
        products_list.extend(qs.all())
    
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 12)

    try:
       products = paginator.page(page)
    except PageNotAnInteger:
       products = paginator.page(1)
    except EmptyPage:
       products = paginator.page(paginator.num_pages)

    ctx = {
        'title': category_detail.name,
        'keywords': 'Недорогие товары, быстрая доставка, Минск, sale',
        'shop_name': SHOP_NAME,
        'categories': list(category_all),
        'products': products,
    }

    return render(request, 'category_details.html', ctx)