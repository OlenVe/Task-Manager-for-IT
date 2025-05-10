from django.test import TestCase
from django.contrib.auth import get_user_model
from tasker.models import Team, TaskType
from tasker.forms import TaskForm

User = get_user_model()


class TaskFormTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")

    def test_task_form_invalid(self):
        form_data = {
            "name": "",  # Name is required
            "description": "Test Description",
            "deadline": "2024-12-31 12:00:00",
            "priority": "Low",
            "task_type": self.task_type.id,
            "team": self.team.id,
        }
        form = TaskForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
