from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from tasker.forms import TaskForm
from tasker.models import Task, Project


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 15
    queryset = Task.objects.all()
    template_name = "tasker/task/task_list.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    fields = "__all__"
    template_name = "tasker/task/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "workers")
    template_name = "tasker/task/task_form.html"

    def get_success_url(self):
        return reverse_lazy("tasker:tasks-list")

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        form.instance.project = project
        form.instance.team = project.team
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = (
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "task_type",
        "workers",
    )
    success_url = reverse_lazy("tasker:tasks-list")
    template_name = "tasker/task/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasker:tasks-list")
    template_name = "tasker/task/task_confirm_delete.html"


def change_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse_lazy("tasker:tasks-list"))
