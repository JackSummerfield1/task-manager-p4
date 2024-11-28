from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRIORITY = ((0, "Low"), (1, "Medium"), (3, "High"))


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
