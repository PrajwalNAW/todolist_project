from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import TodoItem

class TodoItemTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.todo_item = TodoItem.objects.create(title="Test Task", description="Test Description")

    def test_create_todo_item(self):
        response = self.client.post(reverse('todoitem-list'), {'title': 'New Task', 'description': 'New Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_all_todo_items(self):
        response = self.client.get(reverse('todoitem-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_item(self):
        response = self.client.patch(reverse('todoitem-detail', args=[self.todo_item.id]), {'title': 'Updated Task'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo_item(self):
        response = self.client.delete(reverse('todoitem-detail', args=[self.todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
