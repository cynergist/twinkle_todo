from django.db import models
import datetime

class Task(models.Model):
    '''A task the user intends to complete'''
    text = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)

def __str__(self):
    '''Return a string representation of the model.'''
    return self.text

class Entry(models.Model):
    '''The specific parts of a task'''
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
    '''Handles plural references of entry'''
    plural_name = 'entries'

def __str__(self):
    '''Return a string representation of the model.'''
    return f"{self.text[:50]}..."

