from django import forms
from tasker.models import Task
from accounts.models import Worker

class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=False,
        label="Assign Workers"
    )

    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'priority', 'task_type', 'team', 'workers')
        widgets = {
            'deadline': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            'description': forms.Textarea(attrs={"rows": 3, "class": "form-control"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Робимо поле project тільки для читання
        self.fields["project"].disabled = True


