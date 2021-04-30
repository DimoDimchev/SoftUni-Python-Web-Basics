from django.shortcuts import render

from todos_app.forms import TodoForm
from todos_app.models import ToDo


# Create your views here.
def index(request):
    context = {
        'todos': ToDo.objects.all(),
        'todo_form': TodoForm(),
    }
    return render(request, 'todo.html', context)
