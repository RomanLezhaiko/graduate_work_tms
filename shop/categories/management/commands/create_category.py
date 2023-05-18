import json

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from categories.models import Category


class Command(BaseCommand):
    help = 'Fill db categories data.'


    def handle(self, *args, **kwargs):
        categories = []
        with open('/home/roman/dev/git_projects/graduate_work_tms/shop/categories/management/commands/category.json', 'r') as f:
            categories = json.load(fp=f)


        for tmp_dict in categories:
            cat = Category()
            cat.name = tmp_dict['name']
            if tmp_dict['parent_id'] == None:
                cat.parent = tmp_dict['parent_id']
            else:
                parent_category = Category.objects.filter(id=tmp_dict['parent_id']).first()
                cat.parent = parent_category

            try:
                cat.save()
            except IntegrityError:
                cat.name = tmp_dict['name'] + '-another'
                cat.save()

        
        print('All categories was created!')

