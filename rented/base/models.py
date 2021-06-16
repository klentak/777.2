from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.functions import Coalesce


class Genre(models.Model):
    value = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.value


class Author(models.Model):

    class AuthorType(models.TextChoices):
        writer = 'WRITER',
        director = 'DIRECTOR',

    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=40, null=True)
    type = models.CharField(
        max_length=8,
        null=True,
        choices=AuthorType.choices,
    )

    def __str__(self):
        return '%s %s ' % (self.name, self.surname)


class BookManager(models.Manager):
    def with_available(self):
        return self.annotate(
            available=Coalesce(models.Count(), 0)
        )


class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    isbn = models.IntegerField(unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.deletion.DO_NOTHING)
    writer = models.ForeignKey(Author, on_delete=models.deletion.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        unique_together = [['title', 'writer', 'genre']]

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=200, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.deletion.DO_NOTHING)
    duration = models.TimeField()
    director = models.ForeignKey(Author, on_delete=models.deletion.DO_NOTHING)
    amount = models.IntegerField()

    # TODO: liczby różnych filmów danego gatunku w ramach całej kolekcji mogą różnić się o 3
    # TODO: jeżeli reżyser i tytuł się powtarza, to czas trwania musi się różnić

    class Meta:
        unique_together = [['title', 'director', 'duration']]

    def __str__(self):
        return self.title


class Band(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Cd(models.Model):
    title = models.CharField(max_length=200, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.deletion.DO_NOTHING)
    band = models.ForeignKey(Band, on_delete=models.deletion.DO_NOTHING)
    amount = models.IntegerField()
    song_list = models.CharField(max_length=200, null=False)

    class Meta:
        unique_together = [['song_list', 'genre']]


class Rent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    cd = models.ForeignKey(Cd, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rent_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField()

    class Meta:
        order_with_respect_to = 'user'


    # TODO: only one of field [film, book, cd]
    def __str__(self):
        return self.book.__str__()

