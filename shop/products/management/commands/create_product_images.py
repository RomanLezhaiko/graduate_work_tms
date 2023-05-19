import json

from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile

from products.models import Product, ProductImage


class Command(BaseCommand):
    help = 'Fill db products image data.'


    def handle(self, *args, **kwargs):
        images = []
        with open('/home/roman/dev/git_projects/graduate_work_tms/shop/products/management/commands/images_data_final.json', 'r') as f:
            images = json.load(fp=f)
        

        for tmp_dict in images:
            product_image = ProductImage()
            product = Product.objects.get(id=tmp_dict['product_id'])
            product_image.product = product

            f = open(tmp_dict['image_path'], 'rb')
            product_image.image = ImageFile(f)

            product_image.image_width = tmp_dict['width']
            product_image.image_height = tmp_dict['height']

            product_image.save()
            f.close()
        
        print('All images was created!')