from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    title = 'My first Django Project'
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
    }
    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context
