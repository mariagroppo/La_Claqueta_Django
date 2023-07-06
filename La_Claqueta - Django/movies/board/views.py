from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm, BookFilmForm
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.

""" def film_detail(request, id):
    film = get_object_or_404(Film, pk=id)
    context = settings.MEDIA_URL
    return render(request, 'pages/filmDetail.html', {"id": id, "film": film, 'context': context}) """

class FilmDetailView(TemplateView):
    def get(self, request, id):
        film = get_object_or_404(Film, pk=id)
        context = settings.MEDIA_URL
        options = []
        options.append((film.day_1, film.day_1))
        options.append((film.day_2, film.day_2))
        options.append((film.day_3, film.day_3))
        """ Cada opción en la lista es una tupla que contiene el valor y \
              la etiqueta para mostrar en el listado desplegable. """
        form = BookFilmForm(initial={'film': film.title})
        form.fields['schedule'].choices = options
        return render(request, 'pages/filmDetail.html', {"id": id, "film": film, 'context': context, 'form': form})


""" def addFilm(request):
    if request.method == 'GET':
        data = {
            'form' : FilmForm(),
        }
        return render(request, 'pages/addFilmForm.html', data)
    else:
        formulario = FilmForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            
        return redirect('/board') """

class AddFilmView(TemplateView):
    def get(self, request):
        data = {
            'form': FilmForm(),
        }
        return render(request, 'pages/addFilmForm.html', data)

    def post(self, request):
        formulario = FilmForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
        return redirect('/board')

""" def deleteFilm(request, id):
    registro = get_object_or_404(Film, id=id)
    registro.delete()
    return redirect('/board') """

class DeleteFilmView(TemplateView):
    def get(self, request, id):
        registro = get_object_or_404(Film, id=id)
        registro.delete()
        return redirect('/board')

""" def updateFilm(request, id):
    if request.method == 'GET':
        film = get_object_or_404(Film, id=id)
        print(film)
        #film = Film.objects.filter(id=id)
        form = FilmForm(initial=film.__dict__)
        #form = FilmForm(instance=film)
        return render(request, 'pages/updateFilmForm.html', {'form': form, 'film': film})
    else:
        film = get_object_or_404(Film, id=id)
        formulario = FilmForm(request.POST, request.FILES, instance=film)
        if formulario.is_valid():
            formulario.save()
        return redirect('/board') """
    
class UpdateFilmView(TemplateView):
    def get(self, request, id):
        film = get_object_or_404(Film, id=id)
        form = FilmForm(initial=film.__dict__)
        return render(request, 'pages/updateFilmForm.html', {'form': form, 'film': film})

    def post(self, request, id):
        film = get_object_or_404(Film, id=id)
        formulario = FilmForm(request.POST, request.FILES, instance=film)
        if formulario.is_valid():
            formulario.save()
        return redirect('/board')


class BookingFilm(TemplateView):
    def post(self, request):
        form = BookFilmForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha enviado un correo con los pasos a seguir. Muchas gracias por la reserva!')
        else:
            print(form.errors)
        return redirect('/board')