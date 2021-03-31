from django.utils import timezone

from django.test import TestCase

from apps.user.models import User


class UserModelTests(TestCase):

    def test_is_empty(self):
        # check if airport table is empty at first
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 0)

    def test_is_count_one(self):
        # check if count one when a record was created
        user = User(
            username='test user',
            email='test@gmail.com'
        )
        user.save()

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 1)

    def test_saving_and_retrieving_user(self):
        # check if saved value is same as ones before register
        user = User()
        username = 'Test User'
        email = 'teest@gmail.com'
        user.username = username
        user.email = email
        user.save()

        saved_user = User.objects.all()
        actual_user = saved_user[0]

        self.assertEqual(actual_user.username, username)
        self.assertEqual(actual_user.email, email)
