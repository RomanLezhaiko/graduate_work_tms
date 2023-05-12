from django.db import models

from users.models import CustomUser


class CustomerReview(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    customer_review = models.TextField('Отзыв', max_length=4096, blank=False)
    admin_answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DRAFT)


    class Meta:
        ordering = ["-created_at"]


    def __str__(self) -> str:
        return self.customer_review