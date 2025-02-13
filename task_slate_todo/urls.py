from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'task_slate_todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.add_task, name='create_task'),
    path('view_tasks/', views.view_tasks_grids, name='view_tasks_grids'),
    path('task_dashboard/', views.task_dashboard, name='task_dashboard'),
     path('account/', views.profile_view, name='profile'),
]