from django.urls import path
from .views import index, add_film, edit_film, delete_film

app_name = 'crud'

urlpatterns = [
    path('', index, name='index'),
    path('films/add/', add_film, name='add-film'),
    path('films/edit/<int:id>/', edit_film, name='edit-film'),
    path('films/delete/<int:id>/', delete_film, name='delete-film'),
]