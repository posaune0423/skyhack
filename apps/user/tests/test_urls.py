from django.test import TestCase
from django.urls import resolve
from apps.user.views import show


class UrlTests(TestCase):

    def test_user_detail_url(self):
        # check if list url is correct
        view = resolve('/users/1')
        self.assertEqual(view.url_name, 'show')
