from django.urls import path

from tasker.views import (index,
                          PositionListView,
                          PositionCreateView,
                          PositionUpdateView,
                          PositionDetailView,
                          PositionDeleteView,
                          WorkerListView
                          )


app_name = "tasker"




urlpatterns = [
    path("", index, name="index"),
    path("positions/",
         PositionListView.as_view(),
         name="position-list"
         ),
    path("positions/create",
         PositionCreateView.as_view(),
         name="position-create"
         ),
    path("positions/<int:pk>/update/",
         PositionUpdateView.as_view(),
         name="position-update"
         ),
    path("positions/<int:pk>/",
         PositionDetailView.as_view(),
         name="position-detail"
         ),
    path("positions/<int:pk>/delete/",
         PositionDeleteView.as_view(),
         name="position-delete"
         ),
    path("workers/",
         WorkerListView.as_view(),
         name="worker-list"
         ),
    path("workers/create",
         WorkerCreateView.as_view(),
         name="worker-create"
         ),
    path("workers/<int:pk>/update/",
         WorkerUpdateView.as_view(),
         name="worker-update"
         ),
    path("worker/<int:pk>/",
         WorkerDetailView.as_view(),
         name="worker-detail"
         ),
    path("worker/<int:pk>/delete/",
         WorkerDeleteView.as_view(),
         name="worker-delete"
         ),
    ]