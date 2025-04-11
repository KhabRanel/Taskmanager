from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task


def home(request):
    return render(request, 'tasks/home.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    data = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context=data)


