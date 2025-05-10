from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import Team


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 5
    template_name = "tasker/team/team_list.html"


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasker:teams-list")
    template_name = "tasker/team/team_form.html"


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasker:teams-list")
    template_name = "tasker/team/team_form.html"


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    context_object_name = "team"
    success_url = reverse_lazy("tasker:teams-list")
    template_name = "tasker/team/team_confirm_delete.html"
