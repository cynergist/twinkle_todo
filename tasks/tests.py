from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    '''Tests ability to add content to 'text' and 'description' fields'''

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(text='first task')
        Task.objects.create(description='default description here')

    def test_text_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.text}'
        self.assertEquals(expected_object_name, 'first task')

    def test_description_content(self):
        task = Task.objects.get(id=2)
        expected_object_name = f'{task.description}'
        self.assertEquals(expected_object_name, 'default description here')
