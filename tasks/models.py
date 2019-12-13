from django.db import models
import datetime

class Task(models.Model):
    '''A task the user intends to complete'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''Return a string representation of the model.'''
        return self.text

