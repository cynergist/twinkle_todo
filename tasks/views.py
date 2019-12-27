from rest_framework import generics
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

class ListTask(generics.ListCreateAPIView):
    '''Lists all tasks'''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    '''Provides detail view of a single task object'''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def index(request):
    '''The home page for Twinkle Todo'''
    return render(request, 'tasks/index.html')

def tasks(request):
    '''Show all tasks'''
    tasks = Task.objects.order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)
# A context is a dict in which the keys are names we'll use in the template to access data.

def task(request, task_id):
    '''Show a single task and all its entries'''
    task = Task.objects.get(id=task_id)
    entries = task.entry_set.order_by('-date_added')
    context = {'task': task, 'entries': entries}
    return render(request, 'tasks/task.html', context)


def about(request):
    '''The about page for Twinkle Todo'''
    return render(request, 'tasks/about.html')

def contact(request):
    '''The contact page for Twinkle Todo'''
    return render(request, 'tasks/contact.html')




