from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import Team


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    context_object_name = "team_list"
    template_name = "tasker/team/team_list.html"
    paginate_by = 5


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasker:team-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasker:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("tasker:team-list")