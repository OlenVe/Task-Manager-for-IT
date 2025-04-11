from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tasker.models import Task, Worker, Project


@login_required
def index(request):
    """View function for home page of site."""
    
    num_tasks = Task.objects.all().count()
    num_workers = Worker.objects.all().count()
    num_projects = Project.objects.all().count()
    
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
        "num_projects": num_projects,
    }

    return render(request, "tasker/index.html", context)