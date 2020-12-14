from django.urls import path
from .views import (ProjectListView,
ProjectDetailView,
ProjectCreateView,
ProjectUpdateView,
ProjectDeleteView,
TaskCreateView,
TaskDetailView,
TaskUpdateView,
TaskDeleteView
)
from . import views 

urlpatterns = [
    path('',ProjectListView.as_view(),name = 'project-home'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name = 'project-detail'),
    path('project/new/',ProjectCreateView.as_view(),name = 'project-create'),
    path('project/<int:pk>/update',ProjectUpdateView.as_view(),name = 'project-update'),
    path('project/<int:pk>/delete',ProjectDeleteView.as_view(),name = 'project-delete'),
     path('project/<int:pk>/task/',TaskDetailView.as_view(),name = 'task-detail'),
    path('project/task/<int:pk>/update',TaskUpdateView.as_view(),name = 'task-update'),
    path('project/task/<int:pk>/delete',TaskDeleteView.as_view(),name = 'task-delete'),
    path('project/<int:pk>/task/new',TaskCreateView.as_view(),name = 'task-create'),
]