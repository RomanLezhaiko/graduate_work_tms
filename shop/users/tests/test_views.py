from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser
from home.models import CustomerReview


class TestViews(TestCase):
    fixtures = ['users.json']


    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.get(username='admin')
    

    def test_signup_GET(self):
        response = self.client.get(reverse('register_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    

    def test_logout_GET(self):
        response = self.client.get(reverse('logout_user'))
        self.assertEquals(response.status_code, 302)
    

    def test_user_login_GET(self):
        response = self.client.get(reverse('login_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')