from django.urls import path
from books.views import bookview, registerview

app_name = 'books'

urlpatterns = [
    path('livro/cadastrar/', registerview, name='register'),
    path('livro/', bookview, name='book'),
]