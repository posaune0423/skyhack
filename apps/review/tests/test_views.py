from django.test import TestCase
from django.urls import reverse

from apps.airport.models import Airport
from apps.review.models import Review
from apps.user.models import User


class ViewTests(TestCase):
    # Test Class for IndexView
    @classmethod
    def setUpTestData(cls):
        user = User(
            username='test user',
            email='test@gmail.com',
            password='testpass'
        )
        user.save()

        airport = Airport(
            title='Test Airport'
        )
        airport.save()

        review = Review(
            title='test review',
            author=user,
            airport=airport,
            rate=5
        )
        review.save()

    def test_create(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('review:create'))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('review:update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        # check if status code = 200 when send GET request
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.get(reverse('review:delete', args=[1]))
        self.assertEqual(response.status_code, 302)
