from django.contrib import admin

from books.models import Book
from books.models import Author
from books.models import Publisher


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
