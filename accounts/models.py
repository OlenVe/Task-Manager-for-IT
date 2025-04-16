from django.contrib.auth.models import AbstractUser
from django.db import models


class Worker(AbstractUser):
    position = models.ForeignKey("tasker.Position", on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey("tasker.Project", on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey("tasker.Team", on_delete=models.PROTECT, null=True, blank=True, related_name='workers')
