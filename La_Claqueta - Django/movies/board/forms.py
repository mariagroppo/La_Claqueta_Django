from django import forms
from .models import Film, Contact, Booking
from django.core.validators import MinValueValidator, MaxValueValidator

class FilmForm(forms.ModelForm):
    """ Indico a que modelo está relacionado """
    class Meta:
        model = Film
        #fields = ["title", "description", "thumbnail", "gender", "duration", "actors", "director", "estreno", "trailer", "accessAllowed"]
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class BookFilmForm(forms.ModelForm):
    tickets_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '1', 'max': '10'})
    )
    
    schedule = forms.ChoiceField()

    class Meta:
        model = Booking
        fields = '__all__'