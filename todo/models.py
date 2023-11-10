from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django import forms


class Priority(models.Model):
    priority_name = models.CharField(max_length=10)
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"
        ordering = ["pk"]
    def __str__(self):
        return self.priority_name

class State(models.Model):
    state_name = models.CharField(max_length=10)
    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["pk"]
    def __str__(self):
        return self.state_name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Owner")
    task_priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, verbose_name="Priority")
    task_state = models.ForeignKey(State, on_delete=models.CASCADE, null=False, verbose_name="State")
    task_description = models.TextField(verbose_name="Description")
    task_creation_date = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    task_due_date = models.DateTimeField(blank=True, verbose_name="Date Due")
    tags = models.TextField(blank=True)

    class Meta:
        ordering = ['task_creation_date']

    def __str__(self):
        return self.task_name

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = ["priority_name"]

