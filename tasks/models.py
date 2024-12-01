from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRIORITY = ((0, "Low"), (1, "Medium"), (3, "High"))


class Task(models.Model):
    """
    Represents a task associated with a user in the task manager database.

    - user (ForeignKey): Referring to the user who owns the task. Deletes all tasks associated to user if user is deleted from database.
    - title (CharField): Title of the task
    - description (TextField): An optional description of the task.
    - deadline: An optional deadline for the task.
    - priority: The task's priority level (Low, Medium, High). Defaults to Low.
    - completed: Whether the task is completed. Defaults to False.

    Methods:
    - __str__: Returns the task title and the user who created it.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | Created by {self.user}"
