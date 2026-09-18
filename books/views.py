from django.shortcuts import render
from books.models import BookModel


def bookview(request):
    books = BookModel.objects.all()

    return render(
        request,
        'books/index.html',
        {
            'books': books
        }
    )
