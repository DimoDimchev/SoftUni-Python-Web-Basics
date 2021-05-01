from django.shortcuts import render, redirect
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
    form = TodoForm(request.POST)

    if form.is_valid():
        task = ToDo(**form.cleaned_data, is_done=False)
        task.save()
        return redirect('todo index')

    context = {
        'todos': ToDo.objects.all(),
        'todo_form': TodoForm(),
    }

    return render(request, 'todo.html', context)
