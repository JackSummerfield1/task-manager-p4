# forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',
                  'deadline', 'priority', 'completed']

    # Full credit to Pretty Printed on how to style Django
    # Form Fields, specifically the placeholder attr
    # https://www.youtube.com/watch?v=ynToND_xOAM
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update(
            {'placeholder': 'YYYY-MM-DD HH:MM:SS'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Please provide a detailed description. '
             '(Optional)'})
