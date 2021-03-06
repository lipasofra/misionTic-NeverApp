# Generated by Django 3.2.8 on 2021-10-21 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neverappApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameIngredient', models.CharField(max_length=100, verbose_name='Name Ingredient')),
            ],
        ),
        migrations.AlterField(
            model_name='usuariohasmenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='neverappApp.menu'),
        ),
        migrations.AlterField(
            model_name='usuariohasmenu',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MenuHasIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='neverappApp.ingredient')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='neverappApp.menu')),
            ],
        ),
    ]
