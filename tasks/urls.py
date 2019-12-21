'''Defines URL patterns for tasks'''

from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    # Home page
    path('', views.ListTask.as_view()),
    # Detail page
    path('<int:pk>/', views.DetailTask.as_view()),
    # Page that shows all tasks
    path('tasks/', views.tasks, name='tasks'),
    # Detail page for a single task
    path('tasks/<int:task_id>/', views.task, name='task'),
]
