from django.shortcuts import render
from django.template import RequestContext
from settings.base import SHOP_NAME


def handler404(request, *args, **argv):
    response = render(request, '404.html', {'title': '404 Error', 'shop_name': SHOP_NAME})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {'title': '500 Error', 'shop_name': SHOP_NAME})
    response.status_code = 500
    return response