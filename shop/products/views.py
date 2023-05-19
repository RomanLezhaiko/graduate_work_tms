from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib import messages

from categories.models import Category
from .models import Product, ProductReview
from .forms import ProductReviewCreationForm
from settings.base import SHOP_NAME


def list_product(request):
    if request.method == 'POST':
        query = request.POST.get('search', '')
        print(query)
        request.session['search'] = query
    else:
        query = request.session['search']


    category = Category.objects.all()
    products_qs = Product.objects.filter(name__icontains=query)

    page = request.GET.get('page', 1)
    paginator = Paginator(products_qs, 12)

    try:
       products = paginator.page(page)
    except PageNotAnInteger:
       products = paginator.page(1)
    except EmptyPage:
       products = paginator.page(paginator.num_pages)

    ctx = {'title': f'Результат поиска {query}',
           'keywords': 'Недорогие товары, быстрая доставка, Минск, sale',
           'shop_name': SHOP_NAME,
           'categories': list(category),
           'products': products
           }
    
    return render(request, 'product_list.html', ctx)


def get_product_by_slug(request, product_slug: str):
    category_all = Category.objects.all()
    product = get_object_or_404(Product, slug=product_slug)
    reviews = ProductReview.objects.filter(status=ProductReview.STATUS_PUBLISHED)

    if request.method == 'POST':
        form = ProductReviewCreationForm(request.POST)
        url = reverse('product_details_slug', args=(product.slug,))
           
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(request, "Ваш отзыв отправлен." )

            return redirect(url)
        else:
            messages.error(request, 'Нельзя отправить пустой отзыв!')
    else:
        form = ProductReviewCreationForm()

    ctx = {
        'title': product.name,
        'keywords': product.keywords,
        'shop_name': SHOP_NAME,
        'categories': list(category_all),
        'product': product,
        'form': form,
        'reviews': list(reviews),
    }

    return render(request, 'product_details.html', ctx)