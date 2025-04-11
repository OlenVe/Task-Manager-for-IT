from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasker.models import Worker, Task, Project, Position, Team, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    list_filter = UserAdmin.list_filter + ("position", )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "team",
                        "task",
                    )
                },
            ),
        )
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", "description",)
    list_filter = ("deadline", "is_completed", "priority")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("tasks__deadline", "team")


admin.site.register(Position)
admin.site.register(Team)
admin.site.register(TaskType)

