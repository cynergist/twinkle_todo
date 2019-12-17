from django.contrib import admin

from .models import Task, Entry

admin.site.register(Task)
admin.site.register(Entry)

