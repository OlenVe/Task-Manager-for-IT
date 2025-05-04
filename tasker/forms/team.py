from django import forms

from tasker.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
