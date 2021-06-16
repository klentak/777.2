from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Book, Film, Cd, Band, Genre


class SelectProductToRent(LoginView):
    template_name = 'base/select_product_to_rent.html'


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('select_product_to_rent')


class BookList(ListView):
    model = Book


class BookCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'Book.can_create'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'Book.can_update'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'book.can_delete'
    model = Book
    content_type = 'books'
    success_url = reverse_lazy('books')


class CdList(ListView):
    model = Cd


class CdCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'cd.can_create'
    model = Cd
    fields = '__all__'
    success_url = reverse_lazy('cds')


class CdUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'cd.can_update'
    model = Cd
    fields = '__all__'
    success_url = reverse_lazy('cds')


class CdDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'cd.can_delete'
    model = Cd
    content_type = 'cds'
    success_url = reverse_lazy('cds')


class FilmList(ListView):
    model = Film


class FilmCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'film.can_create'
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films')


class FilmUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'film.can_update'
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films')


class FilmDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'film.can_delete'
    model = Film
    content_type = 'films'
    success_url = reverse_lazy('films')


class BandList(ListView):
    model = Band


class BandCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'band.can_create'
    model = Band
    fields = '__all__'
    success_url = reverse_lazy('bands')


class BandUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'band.can_update'
    model = Band
    fields = '__all__'
    success_url = reverse_lazy('bands')


class BandDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'band.can_delete'
    model = Band
    content_type = 'bands'
    success_url = reverse_lazy('bands')


class GenreList(ListView):
    model = Genre


class GenreCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'genre.can_create'
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')


class GenreUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'genre.can_update'
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')


class GenreDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'genre.can_delete'
    model = Genre
    content_type = 'genres'
    success_url = reverse_lazy('genres')


