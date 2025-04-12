from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from tasker.models import Task


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.all()


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = reverse_lazy("tasker:task-list")
    form_class = TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasker:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasker:task-list")