from django.urls import reverse
from rest_framework.test import APITestCase


class UserCreateAPIViewTestCase(APITestCase):
    url = reverse('api:user_create')

    def test_user_invalid_password(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'password',
            'confirm_password': 'password'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_user_create(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'passWord12##',
            'confirm_password': 'passWord12##'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_unique_username_validation(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'passWord12##',
            'confirm_password': 'passWord12##'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)
