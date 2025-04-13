from django.contrib.auth.forms import UserCreationForm

from tasker.models import Worker


class WorkerCreateForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
            "project",
            "team",
        )