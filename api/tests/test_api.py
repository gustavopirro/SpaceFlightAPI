from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class APITestCase(APITestCase):
    def setUp(self):
        self.unauthenticated_client = APIClient()

        self.admin_user = User.objects.create_user('admin' 'test_password!@$&*43')
        self.admin_user.is_superuser = True
        self.admin_user.is_staff = True

        token = Token.objects.create(user=self.admin_user)
        self.authenticated_client = APIClient()
        self.authenticated_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_articles_unauthenticated(self):
        response = self.unauthenticated_client.get(reverse('api:article_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_events_unauthenticated(self):
        response = self.unauthenticated_client.get(reverse('api:event_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_launches_unauthenticated(self):
        response = self.unauthenticated_client.get(reverse('api:launch_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_article_unauthenticated(self):
        response = self.unauthenticated_client.post(reverse('api:article_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_event_unauthenticated(self):
        response = self.unauthenticated_client.post(reverse('api:event_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_launch_unauthenticated(self):
        response = self.unauthenticated_client.post(reverse('api:launch_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_launch_authenticated_invalid_data(self):
        response = self.authenticated_client.post(reverse('api:launch_list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_event_authenticated_valid_data(self):
        response = self.authenticated_client.post(
            reverse('api:event_list'), data={
                "id": 18432,
                "provider": "test_provider_event"
            }, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_launch_authenticated_valid_data(self):
        response = self.authenticated_client.post(
            reverse('api:launch_list'), data={
                "id": 18300,
                "provider": "test_provider_launch"
            }, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
