import datetime

from django.db import models
from django.utils import timezone
''' These are the base models for handling questions and choices.
Each model is represented by a class that subclasses django.db.models.Model.
Each model has some class variables, each representing a database field
in the model.'''

class Question(models.Model):
    ''' Class for creating and publishing a single Question '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
    def __str__(self):
        ''' Readable string representation for interactive modes '''
        return self.question_text

    def was_published_recently(self):
        ''' Method to find recently published questions '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    
class Choice(models.Model):
    ''' Class relating choice to a single Question '''
    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        ''' Readable string representation for interactive modes '''
        return self.choice_text