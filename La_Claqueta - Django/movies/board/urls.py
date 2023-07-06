from django.urls import path
from .views import FilmDetailView, AddFilmView, DeleteFilmView, UpdateFilmView, BookingFilm
from movies.views import BoardPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BoardPage.as_view(), name='board_page'),
    path('<int:id>', FilmDetailView.as_view()),
    path('addFilm', AddFilmView.as_view()),
    path('deleteFilm/<int:id>', DeleteFilmView.as_view()),
    path('updateFilm/<int:id>', UpdateFilmView.as_view()),
    path('booking', BookingFilm.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)