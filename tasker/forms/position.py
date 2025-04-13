from django import forms
from django.contrib.auth.forms import UserCreationForm

from tasker.models import Position


class PositionCreateForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"



class PositionSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="Search by name")

