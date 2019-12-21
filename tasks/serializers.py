from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'text',
            'description',
            'date_added',
            'date_completed',
            'completed',
            'priority',
        )
        model = Task
