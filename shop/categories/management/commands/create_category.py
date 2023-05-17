from django.core.management.base import BaseCommand

from categories.models import Category


# categories = ['Компьютеры и переферия', 'Смартфоны, ТВ и электроника', 'Товары для дома']

categories = [
    {
        'name': 'Компьютеры и переферия',
        'parent_id': None
    },
    {
        'name': 'Смартфоны, ТВ и электроника',
        'parent_id': None
    },
    {
        'name': 'Товары для дома',
        'parent_id': None
    },
    {
        'name': 'Смартфоны, аксессуары',
        'parent_id': 45
    }
]

class Command(BaseCommand):
    help = 'Fill db categories data.'


    def handle(self, *args, **kwargs):
        for tmp_dict in categories:
            cat = Category()
            cat.name = tmp_dict['name']
            if tmp_dict['parent_id'] == None:
                cat.parent = tmp_dict['parent_id']
            else:
                parent_category = Category.objects.filter(id=tmp_dict['parent_id']).first()
                cat.parent = parent_category

            cat.save()
        
        print('All categories was created!')

