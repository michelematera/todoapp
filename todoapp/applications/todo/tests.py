import base64
from django.core.files.base import ContentFile
from django.urls import reverse
from rest_framework.test import APITestCase
from todoapp.applications.account import models as account_models
from todoapp.applications.todo import models as todo_models


class TaskListCreateAPIViewTestCase(APITestCase):
    url = reverse('api:task_list_create')

    def setUp(self):
        username = 'test'
        email = 'test@test.com'
        password = 'passWord12##'
        account_models.User.objects.create_user(username, email, password)
        response = self.client.post(
            path=reverse('token_obtain_pair'),
            data={'username': username, 'password': password},
            format='json'
        )
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))

    def test_task_create(self):
        data = {
            'name': 'task test',
            'description': 'test',
            'deadline': '2019-08-24',
            'image': (
                'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg=='
            )
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

        del data['deadline']

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_task_list(self):
        response = self.client.get(self.url)
        self.assertTrue(200, response.status_code)


class TaskRetrieveUpdateDestroyAPIViewTestCase(APITestCase):

    def setUp(self):
        username = 'test'
        email = 'test@test.com'
        password = 'passWord12##'
        user = account_models.User.objects.create_user(username, email, password)
        self.task = todo_models.Task.objects.create(
            name='task test',
            description='test',
            image=ContentFile(
                base64.b64decode(
                    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg=='
                ),
                name='test.png'
            ),
            user=user
        )
        self.url = reverse('api:task_retrieve_update_destroy', kwargs={'id': self.task.id})
        response = self.client.post(
            path=reverse('token_obtain_pair'),
            data={'username': username, 'password': password},
            format='json'
        )
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))

    def test_task_retrieve(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_task_update(self):
        response = self.client.put(self.url, {'name': 'Test!'})
        self.assertEqual(400, response.status_code)

        data = {
            'name': 'task test 2',
            'description': 'test 4',
            'deadline': '2020-08-24',
            'image': (
                'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg=='
            )
        }

        response = self.client.put(self.url, data)
        self.assertEqual(200, response.status_code)

    def test_task_partial_update(self):
        response = self.client.patch(self.url, {'name': 'Test!'})
        self.assertEqual(200, response.status_code)

    def test_task_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
