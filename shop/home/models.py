from django.db import models

from users.models import CustomUser


class CustomerReview(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_DELETED = 2

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_DELETED, 'Deleted'),
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    customer_review = models.TextField('Отзыв', blank=False)
    admin_answer = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DRAFT)


    class Meta:
        ordering = ["-creation_date"]


    def __str__(self) -> str:
        return self.customer_review