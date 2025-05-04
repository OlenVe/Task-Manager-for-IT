from django import forms

from tasker.models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="Search by name")
