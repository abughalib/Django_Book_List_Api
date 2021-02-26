from rest_framework import serializers
from .models import Author, Book, BookNumber, Characters

class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Characters
    fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id','name']

class BookNumberSerializer(serializers.ModelSerializer):
  class Meta:
    model = BookNumber
    fields = ['id', 'isbn_10', 'isbn_13']

class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer(many=False)
  number = BookNumberSerializer(many=True)
  characters = CharacterSerializer(many=True)
  class Meta:
    model = Book
    fields = ['id', 'title', 'description', 'price', 'published', 'characters', 'number', 'author']