# Generated by Django 3.2.4 on 2021-07-11 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20210712_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]
