from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model: stores author's name
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model: stores title, publication year, and foreign key to Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def clean(self):
        # Ensure publication_year is not in the future
        if self.publication_year > date.today().year:
            raise ValidationError('Publication year cannot be in the future.')

    def __str__(self):
        return self.title
