from django.contrib import admin
from .models import Film, Contact, Booking

# Register your models here.

admin.site.register(Film)
admin.site.register(Contact)
admin.site.register(Booking)