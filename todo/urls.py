from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.main_page, name='main'),
    path('createtask/', views.create_task, name='create'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('sort_tasks/', views.sort_tasks, name='sort_tasks'),
]