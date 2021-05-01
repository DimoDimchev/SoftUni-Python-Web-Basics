from django.urls import path

from todos_app.views import index, create_task

urlpatterns = [
    path('', index, name='todo index'),
    path('create/', create_task, name='create task'),
]
