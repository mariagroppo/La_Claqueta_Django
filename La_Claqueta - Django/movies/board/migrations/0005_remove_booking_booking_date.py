# Generated by Django 4.2.2 on 2023-07-05 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_booking_film_day_1_film_day_2_film_day_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
    ]
