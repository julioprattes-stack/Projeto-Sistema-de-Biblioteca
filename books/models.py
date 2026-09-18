from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    publication_year = models.IntegerField()  #ano publicaçao
    ibsn = models.CharField(max_length=50)
    available = models.BooleanField()  #disponivel
    created_at = models.DateTimeField(auto_now_add=True)  #criado_em

    def __str__(self):
        return f'{self.author} - {self.title}'
