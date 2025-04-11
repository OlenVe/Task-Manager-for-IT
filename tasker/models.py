from django.contrib.auth.models import AbstractUser
from django.db import models


PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Critical", "Critical"),
]

class Position(models.Model):
    name = models.CharField(max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=100)


class TaskType(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Low")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="tasks")
    workers = models.ManyToManyField('Worker', related_name="tasks")


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, related_name='workers')


class Project(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, related_name="projects", on_delete=models.CASCADE)









    
