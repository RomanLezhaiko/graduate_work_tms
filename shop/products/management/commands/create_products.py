import json
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.db.utils import IntegrityError

from products.models import Product
from categories.models import Category


class Command(BaseCommand):
    help = 'Fill db products data.'


    def handle(self, *args, **kwargs):
        products = []
        with open('/home/roman/dev/git_projects/graduate_work_tms/shop/products/management/commands/products_data_final.json', 'r') as f:
            products = json.load(fp=f)


        for tmp_dict in products:
            product = Product()
            product.name = tmp_dict['name']
            category = Category.objects.get(id=tmp_dict['category'])
            product.category = category
            product.keywords = tmp_dict['keywords']
            product.description = tmp_dict['description']
            product.attributes = tmp_dict['attributes']

            f = open(tmp_dict['main_image_path'], 'rb')
            product.main_image = ImageFile(f)


            product.image_width = tmp_dict['image_width']
            product.image_height = tmp_dict['image_height']

            # shop/products/management/commands/images_main

            if tmp_dict['price'] == '':
                product.price = Decimal('200.00')
            else:
                product.price = Decimal(tmp_dict['price'])
            
            try:
                product.save()
            except IntegrityError:
                product.name = tmp_dict['name'] + '-another'
                product.save()
            
            f.close()
        
        print('All products was created!')


