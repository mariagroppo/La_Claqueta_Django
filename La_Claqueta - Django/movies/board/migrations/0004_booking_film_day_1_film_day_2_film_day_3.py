# Generated by Django 4.2.2 on 2023-07-05 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('tickets_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='El valor debe ser igual o mayor que 1.'), django.core.validators.MaxValueValidator(10, message='El valor debe ser igual o menor que 10.')])),
                ('film', models.CharField(default='No title added.', max_length=150, verbose_name='Pelicula')),
                ('schedule', models.CharField(default='No title added.', max_length=150, verbose_name='Agenda')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='day_1',
            field=models.CharField(default=None, max_length=150, verbose_name='Dia 1'),
        ),
        migrations.AddField(
            model_name='film',
            name='day_2',
            field=models.CharField(default=None, max_length=150, verbose_name='Dia 2'),
        ),
        migrations.AddField(
            model_name='film',
            name='day_3',
            field=models.CharField(default=None, max_length=150, verbose_name='Dia 3'),
        ),
    ]
