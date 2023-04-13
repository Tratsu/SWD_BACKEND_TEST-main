from django.contrib import admin
from .models import TodoList as Task


# Register our model
admin.site.register(Task)