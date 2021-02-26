from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  # authentication_classes = (TokenAuthentication, )
  permission_classes = (AllowAny, )
