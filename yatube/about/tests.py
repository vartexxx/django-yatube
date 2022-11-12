from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


User = get_user_model()


class AboutURLTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='user')

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_about_urls__exist_at_desired_location(self):
        """Страница доступна для авторизованного пользователя - автора"""
        urls_collection = {
            reverse(
                'about:author'
            ): HTTPStatus.OK,
            reverse(
                'about:tech'
            ): HTTPStatus.OK,
        }
        for url, http_status in urls_collection.items():
            with self.subTest(address=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, http_status)
