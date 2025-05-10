from django.contrib.auth.forms import UserCreationForm

from accounts.models import Worker


class WorkerForm(UserCreationForm):
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
