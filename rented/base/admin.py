from django.contrib import admin

from .models import Author, Genre, Rent, Book, Cd, Film, Band

admin.site.register(Genre)
admin.site.register(Rent)
admin.site.register(Book)
admin.site.register(Cd)
admin.site.register(Film)
admin.site.register(Band)


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'genre', 'type', 'amount')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')


class IsbnAdmin(admin.ModelAdmin):
    list_display = ('value', 'item')


admin.site.register(Author, AuthorAdmin)
