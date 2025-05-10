from django.urls import path

from tasker.views import (
    index,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDetailView,
    PositionDeleteView,
    WorkerListView,
    WorkerDeleteView,
    WorkerDetailView,
    WorkerUpdateView,
    ProjectListView,
    TeamListView,
    TaskListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    DashboardView,
    ProjectDetailView,
    TaskDetailView,
    change_status,
)


app_name = "tasker"


urlpatterns = [
    path("", DashboardView.as_view(), name="index"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/create/", PositionCreateView.as_view(), name="positions-create"),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="positions-update",
    ),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="positions-detail"),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="positions-delete",
    ),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="workers-update"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers-detail"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="workers-delete"),
    path("projects/", ProjectListView.as_view(), name="projects-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="projects-create"),
    path(
        "projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="projects-update"
    ),
    path(
        "projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="projects-delete"
    ),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="projects-detail"),
    path("teams/", TeamListView.as_view(), name="teams-list"),
    path("teams/create/", TeamCreateView.as_view(), name="teams-create"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="teams-update"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="teams-delete"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path(
        "projects/<int:project_id>/tasks/create/",
        TaskCreateView.as_view(),
        name="tasks-create",
    ),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="tasks-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/change_status/", change_status, name="tasks-change-status"),
    path("task-types/", TaskTypeListView.as_view(), name="task-types-list"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-types-create"),
    path(
        "task-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-types-update",
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-types-delete",
    ),
]
