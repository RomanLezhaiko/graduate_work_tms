from django.core.mail import send_mail
from django.conf import settings

from shop import celery_app


@celery_app.task(bind=True)
def send_email_task(self, *args):
    send_mail(
        args[0],
        args[1],
        settings.EMAIL_HOST_USER,
        [args[2]]
    )
    print('send by celery')