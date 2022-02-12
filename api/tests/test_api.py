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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_launches_unauthenticated(self):
        response = self.unauthenticated_client.get(reverse('api:launch_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

    def test_post_launch_authenticated_duplicated_data(self):
        self.authenticated_client.post(
            reverse('api:launch_list'), data={
                "id": 18300,
                "provider": "test_provider_launch"
            }, format='json'
        )

        response = self.authenticated_client.post(
            reverse('api:launch_list'), data={
                "id": 18300,
                "provider": "test_provider_launch"
            }, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_events_authenticated_invalid_data(self):
        response = self.authenticated_client.post(reverse('api:event_list'))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_article_authenticated_valid_data(self):
        response = self.authenticated_client.post(
            reverse('api:article_list'), data={
                "launches": [
                    {
                        "id": "test_id2",
                        "provider": "test2"
                    },
                    {
                        "id": "test_id",
                        "provider": "test3"
                    }
                ],
                "events": [
                    {
                        "id": "test_id",
                        "provider": "test3"
                    },
                    {
                        "id": "test_id2",
                        "provider": "test4"
                    }
                ],
                "id": 1,
                "title": "updated_title",
                "url": "https://www.testurl.com/",
                "imageUrl": "https://testimg.com",
                "newsSite": "testSite.com",
                "featured": False,
                "summary": "test",
                "publishedAt": "2018-09-10T22:00:00Z",
                "updatedAt": "2021-05-18T13:43:19.938000Z"
            }, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, 201)

    def test_post_article_authenticated_duplicated_valid_data(self):
        post_data = {
            "launches": [
                {
                    "id": "test_id2",
                    "provider": "test2"
                },
                {
                    "id": "test_id",
                    "provider": "test3"
                }
            ],
            "events": [
                {
                    "id": "test_id",
                    "provider": "test3"
                },
                {
                    "id": "test_id2",
                    "provider": "test4"
                }
            ],
            "id": 1,
            "title": "updated_title",
            "url": "https://www.testurl.com/",
            "imageUrl": "https://testimg.com",
            "newsSite": "testSite.com",
            "featured": False,
            "summary": "test",
            "publishedAt": "2018-09-10T22:00:00Z",
            "updatedAt": "2021-05-18T13:43:19.938000Z"
        }

        self.authenticated_client.post(
            reverse('api:article_list'), data=post_data, format='json'
        )

        response = self.authenticated_client.post(
            reverse('api:article_list'), data=post_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_article_authenticated_valid_data(self):
        post_data = {
            "launches": [
                {
                    "id": "test_id2",
                    "provider": "test2"
                },
                {
                    "id": "test_id",
                    "provider": "test3"
                }
            ],
            "events": [
                {
                    "id": "test_id",
                    "provider": "test3"
                },
                {
                    "id": "test_id2",
                    "provider": "test4"
                }
            ],
            "id": 1,
            "title": "updated_title",
            "url": "https://www.testurl.com/",
            "imageUrl": "https://testimg.com",
            "newsSite": "testSite.com",
            "featured": False,
            "summary": "test",
            "publishedAt": "2018-09-10T22:00:00Z",
            "updatedAt": "2021-05-18T13:43:19.938000Z"
        }

        self.authenticated_client.post(
            reverse('api:article_list'), data=post_data, format='json'
        )

        response = self.authenticated_client.put(
            reverse('api:article_detail', args=[1]), data=post_data, format='json'
        )

        launch_obj = self.authenticated_client.get(reverse('api:launch_detail', args=['test_id2']))
        event_obj = self.authenticated_client.get(reverse('api:event_detail', args=['test_id']))

        self.assertEquals(launch_obj.data['id'], 'test_id2')
        self.assertEquals(event_obj.data['id'], 'test_id')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
