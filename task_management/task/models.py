from django.db import models
from datetime import datetime
from category.models import TaskCategory


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=datetime.now)
    category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.task_title
