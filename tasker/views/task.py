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
    form_class = TaskForm
    template_name = 'tasker/task/task_form.html'
    success_url = reverse_lazy('tasker:task-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["project"] = get_object_or_404(Project, id=self.kwargs["project_id"])
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Встановлюємо обов'язкові поля перед збереженням
        form.instance.project = get_object_or_404(Project, id=self.kwargs["project_id"])
        form.instance.created_by = self.request.user
        form.instance.team = self.request.user.team  # Встановлюємо команду з поточного користувача

        try:
            with transaction.atomic():
                # Спочатку зберігаємо основну форму
                response = super().form_valid(form)

                # Якщо є поле workers (ManyToMany), встановлюємо його після збереження
                if hasattr(form.instance, 'workers') and 'workers' in form.cleaned_data:
                    form.instance.workers.set(form.cleaned_data['workers'])

                return response

        except Exception as e:
            print("❌ Помилка при збереженні:", e)
            print("Дані форми:", form.cleaned_data)
            return self.form_invalid(form)

    def form_invalid(self, form):
        print("❌ Помилки валідації форми:")
        print(form.errors)
        return super().form_invalid(form)

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