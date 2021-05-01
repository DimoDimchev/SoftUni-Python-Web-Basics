from django.urls import path

from todos_app.views import index, create_task

urlpatterns = [
    path('', index),
    path('create/', create_task, name='create task'),
]
