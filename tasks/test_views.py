from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TestTaskViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testSuperuser', password='testPassword', email='test@email.com')
        self.task = Task.objects.create(user=self.user, name='test task')

    def login(self):
        self.client.login(username='testSuperuser', password='testPassword')

    def task_list_view_test(self):
        # Testing the login required feature
        response = self.client.get(reverse('task_list'))
        self.assertNotEqual(response.status_code, 200)
