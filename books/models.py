from django.db import models


class AuthorModels(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, blank=True)

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
    publication_year = models.IntegerField()  #ano publicaçao
    ibsn = models.CharField(max_length=50, blank=True)
    available = models.BooleanField(blank=True)  #disponivel
    created_at = models.DateTimeField(auto_now_add=True)  #criado_em

    def __str__(self):
        return f'{self.author} - {self.title}'
