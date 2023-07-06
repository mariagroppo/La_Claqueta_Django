# Generated by Django 4.2.2 on 2023-07-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_film_estreno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=150, verbose_name='Nombre')),
                ('surname', models.CharField(default=None, max_length=150, verbose_name='Apellido')),
                ('message', models.CharField(max_length=2000, verbose_name='Mensaje')),
                ('email', models.EmailField(max_length=254)),
                ('suscribe', models.BooleanField(default=False, verbose_name='Newsletter')),
            ],
        ),
    ]