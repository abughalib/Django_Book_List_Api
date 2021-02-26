from django.db import models
from django.db.models.fields import CharField

class BookNumber(models.Model):
  isbn_10 = models.CharField(max_length=10, blank=True)
  isbn_13 = models.CharField(max_length=10, blank=True)

class Book(models.Model):
  
  title = models.CharField(max_length=50, blank=False, unique=True, default='Book Title')

  description = models.TextField(max_length=256, blank=True)

  published = models.BooleanField(default=False)
  price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
  cover = models.ImageField(upload_to="covers/", blank=True)
  # characters = models.ForeignKey(Characters, blank=True, on_delete=models.SET_NULL)
  number = models.OneToOneField(BookNumber, null=True, blank=True,
    on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Author(models.Model):
  name = models.CharField(max_length=30, default="Ananymous")
  book = models.ManyToManyField(Book, related_name='author')

  def __str__(self):
      return self.name

class Characters(models.Model):
  name = CharField(max_length=30)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="characters")
  def __str__(self):
    return self.name