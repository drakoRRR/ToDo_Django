from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.main_page, name='main'),
    path('createtask/', views.create_task, name='create')
]