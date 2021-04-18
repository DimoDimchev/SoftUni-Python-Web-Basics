from django.contrib import admin
from django.urls import path
from django_101.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
]
