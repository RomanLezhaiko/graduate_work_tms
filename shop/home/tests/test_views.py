from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser
from home.models import CustomerReview


class TestViews(TestCase):
    fixtures = ['users.json']


    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.get(username='admin')
    

    def test_home_page_GET(self):
        response = self.client.get(reverse('home_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')
    

    def test_about_us_page_GET(self):
        response = self.client.get(reverse('about_us_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')


    def test_transport_services_page_GET(self):
        response = self.client.get(reverse('transport_services_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'transport_services.html')
    

    def test_mission_and_values_page_GET(self):
        response = self.client.get(reverse('mission_and_values_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mission_and_values.html')
    

    def test_delivery_page_GET(self):
        response = self.client.get(reverse('delivery_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delivery.html')
    

    def test_equipment_repair_page_GET(self):
        response = self.client.get(reverse('equipment_repair_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'equipment_repair.html')
    

    def test_replacement_and_return_products_GET(self):
        response = self.client.get(reverse('replacement_and_return_products_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'replacement_and_return_products.html')
    

    def test_payment_page_GET(self):
        response = self.client.get(reverse('payment_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment.html')