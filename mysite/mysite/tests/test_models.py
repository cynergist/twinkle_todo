#!/usr/bin/python
import inspect
import unittest
import polls
from polls import templates
Question = polls.models.Question
Choice = polls.models.Choice

class MyTests(unittest.TestCase):
    ''' Tests to check documentation and style of Question and Choice classes '''
    
    @classmethod
    def setUpClass(cls):
        ''' Set up for docstring tests '''
        cls.model_func = inspect.getmembers(Question, inspect.isfunction)
        cls.model_func = inspect.getmembers(Choice, inspect.isfunction)

    def test_instantiate(self):
        ''' Some test using self.foo '''#!/usr/bin/python
import inspect
import unittest
from django.test import TestCase
from polls.models import Question, Choice

class MyTests(unittest.TestCase):
    ''' Tests to check documentation and style of Question and Choice classes '''
    
    @classmethod
    def setUpClass(cls):
        ''' Set up for docstring tests '''
        cls.model_func = inspect.getmembers(Question, inspect.isfunction)
        cls.model_func = inspect.getmembers(Choice, inspect.isfunction)

    def test_instantiate(self):
        ''' Some test using self.foo '''#!/usr/bin/python
import inspect
import unittest
from django.test import TestCase
from polls.models import Question, Choice

class MyTests(unittest.TestCase):
    ''' Tests to check documentation and style of Question and Choice classes '''
    
    @classmethod
    def setUpClass(cls):
        ''' Set up for docstring tests '''
        cls.model_func = inspect.getmembers(Question, inspect.isfunction)
        cls.model_func = inspect.getmembers(Choice, inspect.isfunction)

    def test_instantiate(self):
        ''' Some test '''