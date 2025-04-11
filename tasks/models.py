from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tasks')

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

