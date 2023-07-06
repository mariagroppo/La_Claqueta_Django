from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from board.models import Film
from board.forms import ContactForm
from django.conf import settings

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'pages/landing_page.html'

class BoardPage(TemplateView):
    template_name = 'pages/landing_page.html'
    def get(self, request):
        films = Film.objects.all()
        context = settings.MEDIA_URL
        return render(request, 'pages/board.html', {'films': films, 'context': context, 'user': request.user})

class ContactPage(TemplateView):
    template_name = 'pages/landing_page.html'
    def get(self, request):
        data = {
            'form': ContactForm(),
        }
        return render(request, 'pages/contact.html', data)

    def post(self, request):
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('/board')


