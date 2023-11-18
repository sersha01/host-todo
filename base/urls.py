from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.list_todo, name='list_todo'),
    path('tasks/add/', views.add_todo, name='add_todo'),
    path('tasks/update/<int:pk>', views.update_todo, name='update_todo'),
    path('tasks/delete/<int:pk>', views.delete_todo, name='delete_todo'),
]