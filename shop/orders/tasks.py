from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Order
from settings.base import SHOP_NAME
from shop import celery_app


@celery_app.task(bind=True)
def send_email_task(self, instance_id, email):
    order = Order.objects.get(id=instance_id)
    # print(order.email)
    order_items = order.items.all()

    html_message = render_to_string('order_email.html', {'products': list(order_items), 'total_cost': order.get_total_cost()})

    send_mail(
        f'Ваш заказ в магазине {SHOP_NAME}',
        'Email body text',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
    )


@celery_app.task(bind=True)
def send_email_to_manager_task(self, instance_id):
    send_mail(
        'New order',
        f'You have 1 new order.\nhttp://127.0.0.1:8000/admin/orders/order/{instance_id}/change/',
        settings.EMAIL_HOST_USER,
        ['roman.lezhaiko@gmail.com'],
    )