from django.urls import path
from books.views import bookview, registerview, editview

app_name = 'books'

urlpatterns = [
    path('livro/', bookview, name='book'),
    path('livros/cadastrar/', registerview, name='register'),
    path('livros/editar/<int:id>/', editview, name='edit')
]