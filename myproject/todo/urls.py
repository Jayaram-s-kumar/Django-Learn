from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create', views.create_task, name='create_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('api/tasks', views.get_tasks, name='get_tasks'),
    path('api/addtasks', views.add_task_api, name='add_tasks'),
    path('api/update/<int:pk>/', views.update_task_api, name='update_tasks'),
    path('api/delete/<int:pk>/', views.delete_task_api, name='delete_tasks'),
    
]