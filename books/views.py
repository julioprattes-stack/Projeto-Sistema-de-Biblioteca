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

def editview(request, id):

    book = BookModel.objects.get(id=id)

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('books:book')

    else:
        form = RegisterForm(instance=book)

    return render(
        request,
        'books/edit.html',
        {'form':form}
    )

def deleteview(request, id):

    book = BookModel.objects.get(id=id)

    if request.method == 'POST':
        book.delete()

        return redirect('books:book')

    return render(
        request,
        'books/delete.html',
        {'book':book}
    )

        
