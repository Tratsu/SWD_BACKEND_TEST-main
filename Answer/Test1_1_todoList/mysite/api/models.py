from django.db import models as m

class TodoList(m.Model):
    title           = m.CharField(max_length=20)
    description     = m.TextField()
    completed       = m.BooleanField(default=False)
    created_at      = m.DateTimeField(auto_now_add=True)
    updated_at      = m.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'todo_list'
    
    def __str__(self):
        return self.title