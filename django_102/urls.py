from django.urls import path
from django_102.views import *

urlpatterns = [
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
]
