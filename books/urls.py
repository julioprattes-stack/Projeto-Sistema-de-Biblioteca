from django.urls import path
from books.views import (
    BookCreateView,
    BookDeleteView,
    BookListView,
    BookUpdateView
)

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book'),
    path('new_book', BookCreateView.as_view(), name='register'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='edit'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='delete' ),
]