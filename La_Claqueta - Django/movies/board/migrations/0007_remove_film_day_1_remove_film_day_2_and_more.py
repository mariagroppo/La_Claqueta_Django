# Generated by Django 4.2.2 on 2023-07-05 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_film_day_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='day_1',
        ),
        migrations.RemoveField(
            model_name='film',
            name='day_2',
        ),
        migrations.RemoveField(
            model_name='film',
            name='day_3',
        ),
    ]
