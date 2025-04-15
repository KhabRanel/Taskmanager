from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete')
]