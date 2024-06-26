from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from .models import Library, Book, Shelf, Author



class LibraryAdmin(dj_admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
dj_admin.site.register(Library, LibraryAdmin)

class AuthorAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)
neo_admin.register(Author, AuthorAdmin)

class BookAdmin(dj_admin.ModelAdmin):
    list_display = ("title", "created")
    filter_horizontal = ('authored_by',)
    #fields = ('title', 'shelf')
neo_admin.register(Book, BookAdmin)


class ShelfAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)
neo_admin.register(Shelf, ShelfAdmin)
