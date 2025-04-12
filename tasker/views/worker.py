from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import Worker


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related("tasks")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    success_url = reverse_lazy("tasker:worker-list")
    form_class = WorkerCreationForm


class WorkerUpdateLicenseView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    success_url = reverse_lazy("tasker:worker-list")
    form_class = WorkerTeamUpdateForm
    template_name = "tasker/worker/team_update.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasker:worker-list")


#
# @login_required
# def assign_to_car(request, pk):
#     car = Worker.objects.get(pk=pk)
#     car.drivers.add(request.user)
#     return redirect("taxi:car-detail", pk=pk)
#
#
# @login_required
# def unassign_from_car(request, pk):
#     car = Car.objects.get(pk=pk)
#     car.drivers.remove(request.user)
#     return redirect("taxi:car-detail", pk=pk)