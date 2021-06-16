from django.urls import path
from .views import CustomLoginView, SelectProductToRent, BookList, FilmList, CdList, BookCreate, CdCreate, FilmCreate, \
    BandCreate, BandList, GenreCreate, GenreList, BandDelete, BookUpdate, CdUpdate, FilmUpdate, BandUpdate, GenreUpdate, \
    BookDelete, FilmDelete, GenreDelete, CdDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', SelectProductToRent.as_view(), name='select_product_to_rent'),

    path('books/', BookList.as_view(), name='books'),
    path('book-create/', BookCreate.as_view(), name='book_create'),
    path('book-update/<int:pk>/', BookUpdate.as_view(), name='book_update'),
    path('book-delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),

    path('cds/', CdList.as_view(), name='cds'),
    path('cd-create/', CdCreate.as_view(), name='cd_create'),
    path('cd-update/<int:pk>/', CdUpdate.as_view(), name='cd_update'),
    path('cd-delete/<int:pk>/', CdDelete.as_view(), name='cd_delete'),

    path('films/', FilmList.as_view(), name='films'),
    path('film-create/', FilmCreate.as_view(), name='film_create'),
    path('film-update/<int:pk>/', FilmUpdate.as_view(), name='film_update'),
    path('film-delete/<int:pk>/', FilmDelete.as_view(), name='film_delete'),

    path('bands/', BandList.as_view(), name='bands'),
    path('band-create/', BandCreate.as_view(), name='band_create'),
    path('band-update/<int:pk>/', BandUpdate.as_view(), name='band_update'),
    path('band-delete/<int:pk>/', BandDelete.as_view(), name='band_delete'),

    path('genres/', GenreList.as_view(), name='genres'),
    path('genre-create/', GenreCreate.as_view(), name='genre_create'),
    path('genre-update/<int:pk>/', GenreUpdate.as_view(), name='genre_update'),
    path('genre-delete/<int:pk>/', GenreDelete.as_view(), name='genre_delete'),
]
