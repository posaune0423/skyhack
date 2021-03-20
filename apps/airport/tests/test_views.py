from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    # est Class for IndexView

    def test_home(self):
        # check if status code = 200 when send GET request
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
