from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasker.forms import WorkerForm
from accounts.models import Worker


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 20
    template_name = "tasker/worker/worker_list.html"

    def get_queryset(self):
        return (
            Worker.objects.select_related("position", "project", "team")
            .prefetch_related("tasks", "teams")
            .order_by("username")
        )


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related("tasks")
    template_name = "tasker/worker/worker_detail.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    success_url = reverse_lazy("tasker:workers-list")
    template_name = "tasker/worker/worker_form.html"
    fields = (
        "username",
        "position",
        "team",
    )


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasker:workers-list")
