from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TestTaskViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testSuperuser', password='testPassword', email='test@email.com')
        self.task = Task.objects.create(
            user=self.user,
            title='test task',
            description='test description',
            deadline=None,
            priority=1,
            completed=False
        )

    def login(self):
        self.client.login(username='testSuperuser', password='testPassword')

    def test_task_list_view(self):
        # Testing the login required feature
        response = self.client.get(reverse('task_list'))
        # Should redirect to login page
        self.assertNotEqual(response.status_code, 200)

        # Testing that the correct tasks are displayed
        self.login()
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, 'test task')

    def test_task_create_view(self):
        response = self.client.get(reverse('task_create'))
        # Should redirect to login page
        self.assertNotEqual(response.status_code, 200)

        self.login()
        response = self.client.post(reverse('task_create'), {
            'title': 'task 1',
            'description': 'description 1',
            'deadline': '2024-12-31 00:00:00',
            'priority': 0,
            'completed': False
        })
        self.assertTrue(Task.objects.filter(
            title='task 1', user=self.user).exists())
