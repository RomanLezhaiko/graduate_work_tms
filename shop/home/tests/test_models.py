from django.test import TestCase
from django.db.utils import IntegrityError

from users.models import CustomUser
from home.models import CustomerReview


class TestModels(TestCase):
    fixtures = ['users.json']


    def setUp(self):
        self.user = CustomUser.objects.get(username='admin')
        self.review_1 = CustomerReview.objects.create(
            author=self.user, 
            customer_review='Some text for review.',
        )
    

    def test_customer_review_is_current_user_on_creation(self):
        self.assertEquals(self.review_1.author, self.user)
    

    def test_review_without_author(self):
        with self.assertRaises(IntegrityError):
            CustomerReview.objects.create(customer_review='Some text for review.')