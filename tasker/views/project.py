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
    fields = ("name", "team", "description")
    success_url = reverse_lazy("tasker:projects-list")
    template_name = "tasker/project/project_form.html"


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = ("name", "team", "description")
    success_url = reverse_lazy("tasker:projects-list")
    template_name = "tasker/project/project_form.html"


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasker:projects-list")
    template_name = "tasker/project/project_confirm_delete.html"


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    fields = ("name", "team", "task")
    queryset = Project.objects.all().prefetch_related("team__members")
    template_name = "tasker/project/project_detail.html"
    context_object_name = "project"
