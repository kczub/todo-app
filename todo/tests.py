from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Todo


class TodoModelTests(TestCase):
    def setUp(self):
        Todo.objects.create(title='new', content='lalala')
        Todo.objects.create(title='Wash dishes', content='Serious todo')

    def test_queryset_exists(self):
        qs = Todo.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Todo.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_title_max_lenght(self):
        todo = Todo(title='x'*31, content='x')
        with self.assertRaises(ValidationError):
            todo.full_clean()