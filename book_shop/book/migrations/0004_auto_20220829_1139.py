# Generated by Django 3.2.15 on 2022-08-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_cart_is_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, to='book.BookProduct'),
        ),
        migrations.AlterField(
            model_name='category',
            name='books',
            field=models.ManyToManyField(null=True, to='book.BookProduct'),
        ),
    ]
