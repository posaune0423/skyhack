from django.test import TestCase
from django.urls import resolve
from apps.review.views import Create, Update, delete


class UrlTests(TestCase):

    def test_review_create_url(self):
        # check if list url is correct
        view = resolve('/reviews/create/')
        self.assertEqual(view.func.view_class, Create)

    def test_review_edit_url(self):
        # check if search url is correct
        view = resolve('/reviews/1/edit')
        self.assertEqual(view.func.view_class, Update)

    def test_review_delete_url(self):
        # check if detail url is correct
        view = resolve('/reviews/1/delete')
        self.assertEqual(view.func, delete)
