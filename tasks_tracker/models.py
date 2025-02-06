from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=5
    )
    media = models.FileField(upload_to='comments_media/', blank=True, null=True)

    def __str__(self):
        return self.author
