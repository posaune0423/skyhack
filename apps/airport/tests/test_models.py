from django.test import TestCase
from django.utils import timezone

from apps.airport.models import Airport


class AirportModelTests(TestCase):

    def test_is_empty(self):
        # check if airport table is empty at first
        saved_posts = Airport.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def test_is_count_one(self):
        # check if count one when a record was created
        airport = Airport(
            title='test_airport',
            created_at=timezone.now(),
            rate=5
        )
        airport.save()
        saved_posts = Airport.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_airport(self):
        # check if saved value is same as ones before register
        airport = Airport()
        title = 'Test Airport'
        body = 'Test description'
        created_at = timezone.now()
        rate = 5

        airport.title = title
        airport.body = body
        airport.created_at = created_at
        airport.rate = rate
        airport.save()

        saved_airports = Airport.objects.all()
        actual_airport = saved_airports[0]

        self.assertEqual(actual_airport.title, title)
        self.assertEqual(actual_airport.body, body)
        self.assertEqual(actual_airport.rate, rate)
