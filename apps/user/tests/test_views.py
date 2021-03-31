from django.test import TestCase
from django.urls import reverse
from apps.user.models import User


class ViewTests(TestCase):
    # Test Class for IndexView

    def test_create(self):
        # check if status code = 200 when send GET request
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('mypage:update'))
        self.assertEqual(response.status_code, 200)

    def test_inedx(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('mypage:index'))
        self.assertEqual(response.status_code, 200)
