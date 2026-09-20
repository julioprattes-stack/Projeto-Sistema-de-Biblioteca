from django.shortcuts import render, redirect
from books.models import BookModel
from books.forms import RegisterForm


def bookview(request):
    books = BookModel.objects.all()

    return render(
        request,
        'books/index.html',
        {
            'books': books
        }
    )

def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('books:book')

    else:
        form = RegisterForm()

    return render(
        request,
        'books/register.html',
        {'form':form}
    )