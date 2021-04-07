from django.test import TestCase
from django.urls import reverse

from apps.user.models import User


class ViewTests(TestCase):
    # Test Class for IndexView

    def test_index(self):
        # check if status code = 200 when send GET request
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('airport:search'))
        self.assertEqual(response.status_code, 200)

    def test_top(self):
        # check if status code = 200 when send GET request
        response = self.client.get(reverse('top'))
        self.assertEqual(response.status_code, 200)
