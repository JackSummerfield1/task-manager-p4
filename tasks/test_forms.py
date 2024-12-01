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

    def test_form_is_invalid_with_no_title(self):
        """
        This tests that the form is invalid with no title
        """
        form = TaskForm({
            'description': 'This is a test description',
            'deadline': '2024-12-31 00:00:00',
            'priority': 1,
            'completed': False,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_form_invalid_with_invalid_deadline(self):
        """
        This tests that the form is invalid with an invalid deadline
        """
        form = TaskForm({
            'title': 'Test Task',
            'description': 'This is a test description.',
            'deadline': 'dbajdba',
            'priority': 1,
            'completed': False
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['deadline'], [
                         'Enter a valid date/time.'])
