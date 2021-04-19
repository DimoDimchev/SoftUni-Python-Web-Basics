from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from django_102.models import Game


def test_view(request):
    return HttpResponse("This should return something")


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


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'
