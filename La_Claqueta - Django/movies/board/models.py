from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import URLField, CharField, BooleanField, EmailField, IntegerField, DateField  
from django.db.models.fields.files import ImageField

# Create your models here.
""" Los models indican como se guardan los datos en nuestra BD """

class Film(models.Model):
    title = CharField("Título", max_length=150, default='No title added.')
    description = CharField("Descripcion", max_length=2000, default='No description added.')
    thumbnail = ImageField("Imagen", upload_to='films_board/images/', default='No image added.')
    gender = CharField("Genero", max_length=50, default='No gender added.')
    duration = CharField("Duracion", max_length=50, default='No duration added.')
    actors = CharField("Actores", max_length=200, default='No actors added.')
    director = CharField("Director", max_length=200, default='No director added.')
    estreno = BooleanField("Semana", default=False)
    trailer = URLField("Link Trailer", max_length=1000, default='No trailer added.')
    accessAllowed = CharField("Permiso", max_length=50, default='ATP')
    day_1 = CharField("Dia 1", max_length=150, default=None)
    day_2 = CharField("Dia 2", max_length=150, default=None)
    day_3 = CharField("Dia 3", max_length=150, default=None)

class Contact(models.Model):
    name = CharField("Nombre", max_length=150, default=None)
    surname = CharField("Apellido", max_length=150, default=None)
    message = CharField("Mensaje", max_length=2000, blank=False)
    email = EmailField(blank=False)
    suscribe = BooleanField("Newsletter", default=False)


class Booking(models.Model):
    booking_date = DateField(editable=False, auto_now_add=True)
    email = EmailField(blank=False)
    tickets_quantity = IntegerField(blank=False)
    film =  CharField("Pelicula", max_length=150, default='No film added.', editable=False)
    schedule = CharField("Agenda", max_length=150, default='No schedule added.')