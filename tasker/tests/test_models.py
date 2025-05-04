from django.test import TestCase
from django.contrib.auth import get_user_model
from tasker.models import Position, Task, Team, TaskType

User = get_user_model()


class TaskModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")

    def test_task_creation(self):
        task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2024-12-31",
            priority="Low",
            team=self.team,
            task_type=self.task_type,
        )
        task.workers.add(self.user)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.workers.count(), 1)
