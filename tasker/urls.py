from django.urls import path

from tasker.views import (index,
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
                          ProjectDeleteView, TaskCreateView, TaskDeleteView, TaskUpdateView, TeamCreateView,
                          TeamUpdateView, TeamDeleteView, TaskTypeUpdateView, TaskTypeDeleteView, TaskTypeListView,
                          TaskTypeCreateView, DashboardView, ProjectDetailView, TaskDetailView, change_status,
                          )


app_name = "tasker"




urlpatterns = [
    path("", DashboardView.as_view(), name="index"),
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
    path("projects/",
         ProjectListView.as_view(),
         name="project-list"
         ),
    path("projects/create",
         ProjectCreateView.as_view(),
         name="project-create"
         ),
    path("projects/<int:pk>/update/",
         ProjectUpdateView.as_view(),
         name="project-update"
         ),
    path("projects/<int:pk>/delete/",
        ProjectDeleteView.as_view(),
         name="project-delete"
         ),
    path("projects/<int:pk>/",
         ProjectDetailView.as_view(),
         name="project-detail"
         ),
    path("teams/",
         TeamListView.as_view(),
         name="team-list"
         ),
    path("teams/create/",
         TeamCreateView.as_view(),
         name="team-create"
         ),
    path("teams/<int:pk>/update/",
         TeamUpdateView.as_view(),
         name="team-update"
         ),
    path("teams/<int:pk>/delete/",
         TeamDeleteView.as_view(),
         name="team-delete"
         ),
    path("tasks/",
         TaskListView.as_view(),
         name="task-list"
         ),
    # path("tasks/create/",
    #      TaskCreateView.as_view(),
    #      name="task-create"
    #      ),
    path("projects/<int:project_id>/tasks/create/",
     TaskCreateView.as_view(),
     name="task-create"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"
         ),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path("tasks/<int:pk>/",
         TaskDetailView.as_view(),
         name="task-detail"
         ),
    path("task/<int:pk>/change_status/",
         change_status,
         name="change-status"),
    path("task_types/<int:pk>/update/",
         TaskTypeUpdateView.as_view(),
         name="task_type-update"
         ),
    path("task_types/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(),
         name="task_type-delete"
         ),
    path("task_types/",
         TaskTypeListView.as_view(),
         name="task_type-list"
         ),
    path("task_types/create",
         TaskTypeCreateView.as_view(),
         name="task_type-create"
         ),
    ]