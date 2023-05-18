import os

from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser
from home.models import CustomerReview


class TestViews(TestCase):
    fixtures = ['users.json']


    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.get(username='admin')
    

    def tearDown(self):
        path = '/home/roman/dev/git_projects/graduate_work_tms/shop/shop_cache'
        cache_files = os.listdir(path=path)
        for file in cache_files:
            os.remove(os.path.join(path, file))
    

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
    

    def test_contacts_page_GET(self):
        response = self.client.get(reverse('contacts_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
    

    def test_customer_reviews_page_GET(self):
        response = self.client.get(reverse('customer_reviews_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_reviews.html')
    

    def test_create_review_GET(self):
        response = self.client.get(reverse('review_create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_create.html')
    

    def test_create_review_POST(self):
        self.client.login(username='roman.lezhaiko@gmail.com', password='admin')
        review = 'Добрый день. Хочу поблагодарить за доставку водителя А. Владислава, за быструю доставку. Товар приехал в целостности. Спасибо!'
        response = self.client.post(reverse('review_create'), {
            'customer_review': review,
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomerReview.objects.count(), 1)
    
