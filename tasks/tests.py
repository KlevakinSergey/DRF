
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from .serializers import *



class TestTask(APITestCase):
    def setUp(self):
        Task.objects.create(name='TestTask',  description='TestDescription')

    def test_task_create(self):
        url = reverse('task-create')
        data = {'name': 'Test',
                'description': 'Test'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_tasks_list(self):
        url = reverse('tasks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        task = Task.objects.first()
        url = task.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagTest(APITestCase):
    def setUp(self):
        Tag.objects.create(name='TestTag')


    def test_tag_create(self):
        url = reverse('tag-create')
        data = {'name': 'Test'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tags_list(self):
        url = reverse('tags-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_detail(self):
        tag = Tag.objects.first()
        url = tag.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)