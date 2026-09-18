from django.urls import path
from books.views import bookview

urlpatterns = [
    path('livro/', bookview, name='book'),
]