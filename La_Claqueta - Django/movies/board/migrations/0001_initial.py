# Generated by Django 4.2.2 on 2023-07-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No title added.', max_length=150, verbose_name='Título')),
                ('description', models.CharField(default='No description added.', max_length=2000, verbose_name='Descripcion')),
                ('thumbnail', models.ImageField(default='No image added.', upload_to='films_board/images/', verbose_name='Imagen')),
                ('gender', models.CharField(default='No gender added.', max_length=50, verbose_name='Genero')),
                ('duration', models.CharField(default='No duration added.', max_length=50, verbose_name='Duracion')),
                ('actors', models.CharField(default='No actors added.', max_length=200, verbose_name='Actores')),
                ('director', models.CharField(default='No director added.', max_length=200, verbose_name='Director')),
                ('estreno', models.CharField(default='NO', max_length=2, verbose_name='Semana')),
                ('trailer', models.URLField(default='No trailer added.', max_length=1000, verbose_name='Link Trailer')),
                ('accessAllowed', models.CharField(default='ATP', max_length=50, verbose_name='Permiso')),
            ],
        ),
    ]
