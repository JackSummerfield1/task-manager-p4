from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TestTaskViews(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating a test user and task.
        """
        self.user = User.objects.create_superuser(
            username='testSuperuser', password='testPassword',
            email='test@email.com')
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
        """
        Tests the task list view.

        - Ensures that users are redirected if not logged in
        - Confirms that only tasks associated with the logged
        in user are displayed
        """
        # Testing the login required feature
        response = self.client.get(reverse('task_list'))
        # Should redirect to login page
        self.assertNotEqual(response.status_code, 200)

        # Testing that the correct tasks are displayed
        self.login()  # Logging in the test user
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, 'test task')

    def test_task_create_view(self):
        """
        Tests the task create view.

        - Ensures that users are redirected if not logged in.
        - Ensures that logged in users can create a new task.
        - Confirms the task is saved to the database.
        """
        response = self.client.get(reverse('task_create'))
        # Should redirect to login page
        self.assertNotEqual(response.status_code, 200)

        self.login()  # Logging in the test user
        response = self.client.post(reverse('task_create'), {
            'title': 'task 1',
            'description': 'description 1',
            'deadline': '2024-12-31 00:00:00',
            'priority': 0,
            'completed': False
        })
        self.assertTrue(Task.objects.filter(
            title='task 1', user=self.user).exists())

    def test_task_delete_view(self):
        """
        Tests the task delete view.

        - Ensures that users are redirected if not logged in.
        - Ensures that logged in users can delete an existing task.
        - Confirms the task is removed from the database.
        """
        self.login()  # Logging in the test user

        response = self.client.post(
            reverse('task_delete', kwargs={'pk': self.task.pk}))
        # Ensures that redirection happens
        self.assertEqual(response.status_code, 302)
        # Task should no longer be in the list
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
