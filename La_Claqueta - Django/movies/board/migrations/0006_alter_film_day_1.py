# Generated by Django 4.2.2 on 2023-07-05 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_remove_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='day_1',
            field=models.CharField(max_length=150, verbose_name='Dia 1'),
        ),
    ]
