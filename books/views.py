from django.shortcuts import render


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
        # save form
        pass


def edit(request, pk):
    pass
