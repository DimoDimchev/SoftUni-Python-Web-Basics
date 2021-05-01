from django.shortcuts import render
from django.views.decorators.http import require_POST

from todos_app.forms import TodoForm
from todos_app.models import ToDo


# Create your views here.
def index(request):
    context = {
        'todos': ToDo.objects.all(),
        'todo_form': TodoForm(),
    }
    return render(request, 'todo.html', context)


@require_POST
def create_task(request):
    pass