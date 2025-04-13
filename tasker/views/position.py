from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasker.forms.position import PositionSearchForm, PositionCreateForm
from tasker.models import Position


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    queryset = Position.objects.all()
    template_name = "tasker/position/position_list.html"
    context_object_name = "position_list"
    paginate_by = 10

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = PositionSearchForm(
            initial={"name": name}
        )
        return context


    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Position.objects.filter(name__icontains=name)
        return self.queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionCreateForm
    success_url = reverse_lazy("tasker:position-list")
    template_name = "tasker/position/position_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionCreateForm
    success_url = reverse_lazy("tasker:position-list")
    template_name = "tasker/position/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasker:position-list")
    template_name = "tasker/position/position_confirm_delete.html"


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    queryset = Position.objects.all().select_related("worker")
