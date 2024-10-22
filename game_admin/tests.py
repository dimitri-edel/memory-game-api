from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

import os
from memory_game_api import env
from game_admin.authentication import User

# Test case for UserLoginView
class UserLoginViewTest(APITestCase):
    def setUp(self):
        self.user = User()
        self.url = reverse('user_login_view')
        self.valid_payload = {
            'username': os.environ["ADMIN_USERNAME"],
            'password': os.environ["ADMIN_PASSWORD"]
        }
        self.invalid_payload = {
            'username': 'invalid',
            'password': 'invalid'
        }

    def test_login_user(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token1' in response.data)
        self.assertTrue('token2' in response.data)

    def test_login_user_invalid(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse('token1' in response.data)
        self.assertFalse('token2' in response.data)


