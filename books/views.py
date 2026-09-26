from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from books.models import BookModel
from books.forms import RegisterForm


def bookview(request):

    search = request.GET.get('search', '')

    if search:
        books = BookModel.objects.filter(
            Q(title__icontains=search) |
            Q(author__name__icontains=search)
        )
    else:
        books = BookModel.objects.all()

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'books/index.html',
        {
            'books': page_obj,
            'search': search
        }
    )

def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('books:book')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')

    else:
        form = RegisterForm()

    return render(
        request,
        'books/register.html',
        {'form':form}
    )

def editview(request, id):

    book = get_object_or_404(BookModel, id=id)

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('books:book')
        else:
            messages.error(request, 'Erro ao atualizar. Verifique os dados.')

    else:
        form = RegisterForm(instance=book)

    return render(
        request,
        'books/edit.html',
        {'form':form}
    )

def deleteview(request, id):

    book = get_object_or_404(BookModel, id=id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('books:book')

    return render(
        request,
        'books/delete.html',
        {'book':book}
    )

        
