from django.views.generic import TemplateView
from tasker.models import Task, Project
from accounts.models import Worker
from django.db.models import Count

class DashboardView(TemplateView):
    template_name = "tasker/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Tasks
        tasks = Task.objects.all()
        context["total_tasks"] = tasks.count()
        context["completed_tasks"] = tasks.filter(is_completed=True).count()
        context["active_tasks"] = tasks.filter(is_completed=False).count()
        context["high_priority_tasks"] = tasks.filter(priority="high").count()
        context["low_priority_tasks"] = tasks.filter(priority="low").count()

        #tasks deadline
        tasks_deadline = Task.objects.order_by('deadline')
        context["tasks_deadline"] = Task.objects.order_by('deadline')

        # Workers
        workers = Worker.objects.all()
        context["total_workers"] = workers.count()
        context["workers_by_position"] = dict(
            workers.values_list("position").annotate(count=Count("id")).values_list("position", "count")
        )
        # projects
        projects = Project.objects.select_related("team").prefetch_related("tasks").all()
        project_data = []

        for project in projects:
            total_tasks = project.tasks.count()
            completed_tasks = project.tasks.filter(is_completed=True).count()

            if total_tasks > 0:
                completion_percentage = int((completed_tasks / total_tasks) * 100)
            else:
                completion_percentage = 0

            project_data.append({
                "project": project,
                "completion_percentage": completion_percentage
            })

        context["project_data"] = project_data

        return context