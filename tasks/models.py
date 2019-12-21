from django.db import models
import datetime

class Task(models.Model):
    '''A task the user intends to complete'''
    text = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(blank=True, null=True) # null=True, default=True
    
def __str__(self):
    '''Return a string representation of the model.'''
    return self.text

class Entry(models.Model):
    '''The specific parts of a task'''
    class Meta:
        verbose_name_plural = "entries"
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    '''Return a string representation of the model.'''
    return f"{self.text[:50]}..."

