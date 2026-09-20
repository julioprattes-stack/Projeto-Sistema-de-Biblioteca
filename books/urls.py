from django.urls import path
from books.views import bookview, registerview, editview, deleteview

app_name = 'books'

urlpatterns = [
    path('livro/', bookview, name='book'),
    path('livros/cadastrar/', registerview, name='register'),
    path('livros/editar/<int:id>/', editview, name='edit'),
    path('livros/excluir/<int:id>/', deleteview, name='delete' ),
]