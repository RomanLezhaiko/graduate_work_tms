from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser


class TestViews(TestCase):
    fixtures = ['users.json', 'category.json', 'products.json']


    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.get(username='admin')
    

    # def test_list_product_GET(self):
    #     response = self.client.get(reverse('product_list', args=('Lg',)))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'product_list.html')
    

    def test_product_by_slug_GET(self):
        url = reverse('product_details_slug', args=('kholodilnik-s-morozilnikom-lg-doorcooling-gw-b509clzm',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_details.html')