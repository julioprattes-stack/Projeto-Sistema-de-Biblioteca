from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class AuthorModels(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        AuthorModels,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    category = models.CharField(max_length=50, blank=True)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1400), MinValueValidator(date.today().year)]
    )
    isbn = models.CharField(
        unique=True,
        max_length=50,
        blank=True,
        null=True
    )
    available = models.BooleanField(
        default=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)  #criado_em

    def __str__(self):
        return f'{self.author} - {self.title}'
