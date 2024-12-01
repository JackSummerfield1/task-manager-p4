from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import TaskForm


class TestTaskForm(TestCase):

    def test_form_is_valid(self):
        """Tests that the form is valid"""
        form = TaskForm({
            'title': 'Test Task',
            'description': 'This is a test description.',
            'deadline': '2024-12-31 00:00:00',
            'priority': 1,
            'completed': False
        })
        self.assertTrue(form.is_valid())
