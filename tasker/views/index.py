from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tasker.models import Worker, Project, Task, Team


@login_required
def index(request):
    """View function for the home page of the site."""

    num_worker = Worker.objects.count()
    num_project = Project.objects.count()
    num_task = Task.objects.count()
    num_team = Team.objects.count()




    context = {
        "num_worker": num_worker,
        "num_project": num_project,
        "num_task": num_task,
        "num_team": num_team,
    }

    return render(request, "tasker/index.html", context=context)
