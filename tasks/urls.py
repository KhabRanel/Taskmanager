from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list')
]