from django.db import models
from django.urls import reverse
from django.utils import timezone

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_duration =models.IntegerField(default=0)

    def __str__(self):
        return self.project_title
    
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_start = models.DateField()
    task_end = models.DateField()
    project_id = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.task_name
    
    def get_absolute_url(self):
        return reverse("task-detail", kwargs=({"pk":self.pk}))