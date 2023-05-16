# Generated by Django 4.2 on 2023-05-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('keywords', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('attributes', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('main_image', models.ImageField(upload_to='static/images')),
                ('image_width', models.PositiveIntegerField()),
                ('image_height', models.PositiveIntegerField()),
                ('slug', models.SlugField(blank=True, max_length=128, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('image_width', models.PositiveIntegerField()),
                ('image_height', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_review', models.TextField(verbose_name='Отзыв')),
                ('admin_answer', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
