from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from .models import Project,Task
# Create your views here.
class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name='project/home.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all() 
        print(context)
        return context

class ProjectCreateView(CreateView):
    model = Project
    fields =['project_title','project_description','project_duration']
    def form_valid(self,form):
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    fields =['project_title','project_description','project_duration']

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/' 


class TaskDetailView(DetailView):
    model = Task
    template_name = 'project/task_detail.html'
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        x= self.kwargs['pk']
        context["tasks"] = Task.objects.filter(id=x).first 
        return context

class TaskCreateView(CreateView):
    model = Task
    fields =['task_name','task_description','task_start','task_end','project_id']
    def form_valid(self,form):
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields =['task_name','task_description','task_start','task_end','project_id']

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/' 