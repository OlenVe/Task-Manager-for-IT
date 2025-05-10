from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasker.models import Position, Task, Team, TaskType, Project

User = get_user_model()


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123", is_staff=True
        )
        self.position = Position.objects.create(name="Developer")
        self.team = Team.objects.create(name="Test Team")
        self.project = Project.objects.create(
            name="Test Project", description="Test Description", team=self.team
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.client.login(username="testuser", password="testpass123")

    def test_position_list_view(self):
        response = self.client.get(reverse("tasker:positions-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasker/position/position_list.html")
        self.assertContains(response, self.position.name)

    def test_task_create_view(self):
        task_data = {
            "name": "Test Task",
            "description": "Test Description",
            "deadline": "2024-12-31 12:00:00",
            "priority": "Low",
            "task_type": self.task_type.id,
            "team": self.team.id,
            "workers": [self.user.id],
        }
        response = self.client.post(
            reverse("tasker:tasks-create", kwargs={"project_id": self.project.id}),
            task_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="Test Task").exists())
