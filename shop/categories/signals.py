from unidecode import unidecode

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Category


@receiver(pre_save, sender=Category)
def gen_slug_field(sender, instance, **kwargs):
    if instance.parent is None:
        instance.slug = slugify(unidecode(instance.name))
    else:
        instance.slug = slugify(unidecode(instance.parent.name + '_' + instance.name))