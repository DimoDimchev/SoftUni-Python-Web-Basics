from django.shortcuts import render
from todos_app.models import ToDo


# Create your views here.
def index(request):
    context = {
        'todos': ToDo.objects.all(),
    }
    return render(request, 'todo.html', context)
