# Generated by Django 3.2.8 on 2021-10-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neverappApp', '0002_auto_20211021_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='nameIngredient',
            field=models.CharField(max_length=100, verbose_name='nameIngredient'),
        ),
    ]
