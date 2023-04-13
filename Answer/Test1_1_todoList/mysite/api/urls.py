from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='todo_list_create'),
    path('<int:pk>/', TaskDetail.as_view(), name='todo_retrieve_update_delete'),
]