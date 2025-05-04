from django.contrib.auth.forms import UserCreationForm
from accounts.models import Worker


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )