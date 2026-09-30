from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.db.models import Q
from books.models import BookModel
from books.forms import RegisterForm


class BookListView(ListView):
    model = BookModel
    template_name = 'books/index.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__name__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context
    

class BookCreateView(LoginRequiredMixin, CreateView):
    model = BookModel
    form_class = RegisterForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('books:book')

    def form_valid(self, form):
        messages.success(self.request, 'Livro cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar. Verifique os dados.')
        return super().form_invalid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = BookModel
    form_class = RegisterForm
    template_name = 'books/edit.html'
    success_url = reverse_lazy('books:book')

    def form_valid(self, form):
        messages.success(self.request, 'Livro atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar. Verifique os dados.')
        return super().form_invalid(form)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = BookModel
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:book')

    def form_valid(self, form):
        messages.success(self.request, 'Livro excluído com sucesso!')
        return super().form_valid(form)


# def bookview(request):

#     search = request.GET.get('search', '')

#     if search:
#         books = BookModel.objects.filter(
#             Q(title__icontains=search) |
#             Q(author__name__icontains=search)
#         )
#     else:
#         books = BookModel.objects.all()

#     paginator = Paginator(books, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         'books/index.html',
#         {
#             'books': page_obj,
#             'search': search
#         }
#     )
        
# @login_required
# def registerview(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Livro cadastrado com sucesso!')
#             return redirect('books:book')
#         else:
#             messages.error(request, 'Erro ao cadastrar. Verifique os dados.')

#     else:
#         form = RegisterForm()

#     return render(
#         request,
#         'books/register.html',
#         {'form':form}
#     )

# @login_required
# def editview(request, id):

#     book = get_object_or_404(BookModel, id=id)

#     if request.method == 'POST':
#         form = RegisterForm(request.POST, instance=book)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Livro atualizado com sucesso!')
#             return redirect('books:book')
#         else:
#             messages.error(request, 'Erro ao atualizar. Verifique os dados.')

#     else:
#         form = RegisterForm(instance=book)

#     return render(
#         request,
#         'books/edit.html',
#         {'form':form}
#     )

# @login_required
# def deleteview(request, id):

#     book = get_object_or_404(BookModel, id=id)

#     if request.method == 'POST':
#         book.delete()
#         messages.success(request, 'Livro excluído com sucesso!')
#         return redirect('books:book')

#     return render(
#         request,
#         'books/delete.html',
#         {'book':book}
#     )