from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import TaskType


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    queryset = TaskType.objects.all()
    context_object_name = "task_type_list"
    template_name = "tasker/task_type/task_type_list.html"
    paginate_by = 10


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasker:task-types-list")
    template_name = "tasker/task_type/task_type_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasker:task-types-list")
    template_name = "tasker/task_type/task_type_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasker:task-types-list")
    template_name = "tasker/task_type/task_type_confirm_delete.html"
