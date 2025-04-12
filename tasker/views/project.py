from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import Project


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "tasker/project/project_list.html"
    paginate_by = 5


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasker:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasker:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasker:project-list")