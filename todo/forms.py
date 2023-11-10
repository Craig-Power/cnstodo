from django import forms
from django.forms import ModelForm, widgets
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["task_name", "task_due_date", "task_state", "task_priority", "task_description", "tags"]
        exclude = ["task_creation_date"]
        widgets = {
            'task_due_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }


