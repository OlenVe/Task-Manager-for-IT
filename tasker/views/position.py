from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasker.models import Position


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    queryset = Position.objects.all()
    template_name = "tasker/position/position_list.html"
    context_object_name = "positions_list"
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