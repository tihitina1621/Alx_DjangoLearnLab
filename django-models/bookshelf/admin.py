from django.contrib import admin
from .models import Book

class BookCustom(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author') 

admin.site.register(Book, BookCustom)

# Register your models here.
