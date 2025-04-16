from django.conf import settings
from django.db import models


PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Critical", "Critical"),
]

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField("accounts.Worker", related_name="teams")

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Low")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="tasks")
    workers = models.ManyToManyField("accounts.Worker", related_name="tasks")
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    discussion = models.ForeignKey('Discussion',
                                   on_delete=models.CASCADE,
                                   related_name="tasks",
                                   null=True,
                                   blank=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Discussion(models.Model):
    text = models.TextField(blank=False, help_text="Text of the message")
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the message was created"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="User who sent the message",
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        help_text="Chat room where the message was sent",
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.text[:50]}..."






    
