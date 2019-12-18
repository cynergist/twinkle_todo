from django.shortcuts import render
from .models import Task

def index(request):
    '''The home page for Twinkle Todo'''
    return render(request, 'tasks/index.html')

def tasks(request):
    '''Show all tasks'''
    tasks = Task.objects.order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)

def about(request):
    '''The about page for Twinkle Todo'''
    return render(request, 'tasks/about.html')

def contact(request):
    '''The contact page for Twinkle Todo'''
    return render(request, 'tasks/contact.html')




