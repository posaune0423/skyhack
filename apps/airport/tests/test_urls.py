from django.test import TestCase
from django.urls import resolve
from apps.airport.views import Index, Search, show


class UrlTests(TestCase):

    def test_airport_list_url(self):
        # check if list url is correct
        view = resolve('/home/')
        self.assertEqual(view.func.view_class, Index)

    def test_airport_search_url(self):
        # check if search url is correct
        view = resolve('/airports/search/')
        self.assertEqual(view.func.view_class, Search)

    def test_airport_detail_url(self):
        # check if detail url is correct
        view = resolve('/airports/1')
        self.assertEqual(view.func, show)
