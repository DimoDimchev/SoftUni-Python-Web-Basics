from django.shortcuts import render, redirect

# Create your views here.
from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'books/index.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            'form': BookForm(),
        }
        return render(request, 'books/create.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(request, 'books/create.html', context)


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        context = {
            'form': form,
        }
        return render(request, 'books/edit.html', context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(request, 'books/edit.html', context)
