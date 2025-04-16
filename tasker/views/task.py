from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from tasker.forms import TaskForm
from tasker.models import Task, Project


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.all()
    template_name = "tasker/task/task_list.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    fields = "__all__"
    template_name = "tasker/task/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasker/task/task_form.html'
    success_url = reverse_lazy('tasker:task-list')

    def form_valid(self, form):
        # Якщо форма дійсна, ми створюємо завдання
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Task'
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ("name", "description", "deadline", "is_completed", "priority", "task_type", "workers")
    success_url = reverse_lazy("tasker:task-list")
    template_name = "tasker/task/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasker:task-list")
    template_name = "tasker/task/task_confirm_delete.html"


def change_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse_lazy("tasker:task-list"))