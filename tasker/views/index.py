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
        context["high_priority_tasks"] = tasks.filter(priority="High").count()
        context["critical_priority_tasks"] = tasks.filter(priority="Critical").count()

        # tasks deadline
        context["tasks_deadline"] = Task.objects.order_by("deadline")

        # Workers
        workers_by_position = Worker.objects.values("position__name").annotate(
            count=Count("id")
        )

        # List of workers
        position_count = {
            worker["position__name"]: worker["count"] for worker in workers_by_position
        }
        context["workers_by_position"] = position_count
        context["total_workers"] = Worker.objects.count()

        # Projects
        projects = (
            Project.objects.select_related("team").prefetch_related("tasks").all()
        )
        project_data = []

        for project in projects:
            total_tasks = project.tasks.count()
            completed_tasks = project.tasks.filter(is_completed=True).count()

            if total_tasks > 0:
                completion_percentage = int((completed_tasks / total_tasks) * 100)
            else:
                completion_percentage = 0

            project_data.append(
                {"project": project, "completion_percentage": completion_percentage}
            )

        context["project_data"] = project_data

        return context
