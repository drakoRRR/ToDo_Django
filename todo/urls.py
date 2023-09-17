from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.main_page, name='main'),
    path('createtask/', views.create_task, name='create'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]