# Generated by Django 3.2.4 on 2021-07-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210710_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texts',
            field=models.CharField(default='No text added', max_length=3000, verbose_name='Enter text'),
        ),
    ]
