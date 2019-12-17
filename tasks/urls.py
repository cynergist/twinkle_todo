'''Defines URL patterns for tasks'''

from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
