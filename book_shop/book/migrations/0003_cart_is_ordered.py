# Generated by Django 3.2.15 on 2022-08-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_cart_is_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]