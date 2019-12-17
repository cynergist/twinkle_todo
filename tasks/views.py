from django.shortcuts import render

def index(request):
    '''The hompe page for Twinkle Todo'''
    return render(request, 'tasks/index.html')
