from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=150, choices=[
        ("todo", "To Do"),
        ("inprogress", "In Progress"),
        ("done", "Done"),
    ])
    priority = models.CharField(max_length=150, choices=[
        ('low', "Low"),
        ('medium', "Meduim"),
        ('high', "High"),
        ('critical', 'Critical')
    ])
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title