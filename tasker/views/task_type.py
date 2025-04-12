from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import TaskType


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_pyte_list"
    template_name = "tasker/task_type/task_type_list.html"
    paginate_by = 5


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasker:task_type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasker:task_type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasker:task_type-list")