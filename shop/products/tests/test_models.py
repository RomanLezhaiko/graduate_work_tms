from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from users.models import CustomUser
from products.models import Product, ProductReview, ProductImage
from categories.models import Category


class TestViews(TestCase):
    fixtures = ['users.json', 'category_test.json']


    def setUp(self):
        self.user = CustomUser.objects.get(username='admin')
        self.product_1 = Product.objects.create(
            name='Some name',
            category=Category.objects.get(id=4),
            keywords='some, text',
            description='Some description about product',
            attributes={'key':'value'},
            price=2099.00,
            main_image='static/images/3_ffd4hNh.webp',
            image_width=188,
            image_height=400,
        )

        self.product_image_1 = ProductImage.objects.create(
            product=self.product_1,
            image='static/images/2_pa1RZez.webp',
            image_width=200,
            image_height=400,
        )

        self.review_1 = ProductReview.objects.create(
            author=self.user, 
            product=self.product_1,
            product_review='Some text for review.',
        )


    def test_event_is_assigned_slug_on_creation(self):
        self.assertEquals(self.product_1.slug, 'some-name')

    
    def test_unique_product_slug(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name='Some name',
                category=Category.objects.get(id=4),
                keywords='some, text',
                description='Some description about product',
                attributes={'key':'value'},
                price=2099.00,
                main_image='static/images/3_ffd4hNh.webp',
                image_width=188,
                image_height=400,
            )
    

    def test_add_product_without_category(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name='Some name 2',
                keywords='some, text',
                description='Some description about product',
                attributes={'key':'value'},
                price=2099.00,
                main_image='static/images/3_ffd4hNh.webp',
                image_width=188,
                image_height=400,
            )
    

    def test_add_product_with_wrong_price(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name='Some name 2',
                category=Category.objects.get(id=4),
                keywords='some, text',
                description='Some description about product',
                attributes={'key':'value'},
                price='sdgvskjkjsgvfjkj',
                main_image='static/images/3_ffd4hNh.webp',
                image_width=188,
                image_height=400,
            )
    

    def test_add_image_without_product(self):
        with self.assertRaises(IntegrityError):
            ProductImage.objects.create(
                image='static/images/2_pa1RZez.webp',
                image_width=200,
                image_height=400,
            )


    def test_review_without_author(self):
        with self.assertRaises(IntegrityError):
            ProductReview.objects.create(product=self.product_1, product_review='Some text for review.')
    

    def test_review_without_product(self):
        with self.assertRaises(IntegrityError):
            ProductReview.objects.create(author=self.user, product_review='Some text for review.')