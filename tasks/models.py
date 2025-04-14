from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (NEW, 'Новая'),
        (IN_PROGRESS, 'В работе'),
        (COMPLETED, 'Выполнено'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус',
        choices=STATUS_CHOICES,
        default=NEW)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Дедлайн')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tasks')

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

