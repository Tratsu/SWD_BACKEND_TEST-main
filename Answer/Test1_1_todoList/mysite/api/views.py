from django.shortcuts import render
from .serializers import TaskSerializer
from .models import TodoList as Task
from rest_framework import generics, permissions


class TaskList(generics.ListAPIView):
    queryset            = Task.objects.all()
    serializer_class    = TaskSerializer
    permission_classes  = [permissions.IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Task.objects.all()
    serializer_class    = TaskSerializer