# Generated by Django 3.2.15 on 2022-08-29 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20220829_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(blank=True, to='book.BookProduct'),
        ),
        migrations.AlterField(
            model_name='category',
            name='books',
            field=models.ManyToManyField(to='book.BookProduct'),
        ),
    ]
