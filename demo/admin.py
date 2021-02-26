from django.contrib import admin
from .models import Author, Book, BookNumber, Characters

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ['title', 'description']
  list_filter = ['title']
  search_fields=['title']

@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
  list_display = ['isbn_10', 'isbn_10']
  list_filter = ['isbn_10', 'isbn_10']
  search_fields = ['isbn_10', 'isbn_10']

admin.site.register(Author)
admin.site.register(Characters)