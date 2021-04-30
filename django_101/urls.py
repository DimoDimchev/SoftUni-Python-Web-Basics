from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_102.urls')),
    path('todo/', include('todos_app.urls')),
]
