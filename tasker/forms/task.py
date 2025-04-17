
from django import forms
from django.contrib.auth import get_user_model
from django.forms import HiddenInput

from tasker.models import Task
from accounts.models import Worker

User = get_user_model()

# class TaskForm(forms.ModelForm):
#     workers = forms.ModelMultipleChoiceField(
#         queryset=User.objects.none(),  # тимчасово порожній
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop("user")
#         project = kwargs.pop("project", None)
#         super().__init__(*args, **kwargs)
#
#         if project:
#             self.fields["project"].initial = project
#             self.fields["project"].disabled = True  # ✅ видно, але не можна змінити
#             self.instance.project = project
#
#         if user.team:
#             self.fields["workers"].queryset = User.objects.filter(team=user.team)
#         else:
#             self.fields["workers"].queryset = User.objects.none()

class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),  # тимчасово порожній
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        project = kwargs.pop("project", None)
        super().__init__(*args, **kwargs)

        if project:
            self.fields["project"].initial = project
            self.fields["project"].disabled = True
            self.instance.project = project  # встановлюємо проект для форми

        if user.team:
            self.fields["workers"].queryset = user.team.workers.all()  # або user.team.members.all()
        else:
            self.fields["workers"].queryset = User.objects.none()

    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'priority', 'task_type', 'team', 'workers', 'project')
        widgets = {
            'deadline': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            'description': forms.Textarea(attrs={"rows": 3, "class": "form-control"})
        }

#
# class Meta:
#     model = Task
#     fields = ('name', 'description', 'deadline', 'priority', 'task_type', 'team', 'workers', "project")
#     widgets = {
#         'deadline': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
#         'description': forms.Textarea(attrs={"rows": 3, "class": "form-control"})
#     }



