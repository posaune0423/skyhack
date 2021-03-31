from django.utils import timezone

from django.test import TestCase

from apps.airport.models import Airport
from apps.review.models import Review
from apps.user.models import User


class ReviewModelTests(TestCase):

    def test_is_empty(self):
        # check if airport table is empty at first
        saved_review = Review.objects.all()
        self.assertEqual(saved_review.count(), 0)

    def test_is_count_one(self):
        # check if count one when a record was created
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
        saved_posts = Review.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_review(self):
        # check if saved value is same as ones before register
        review = Review()
        title = 'Test Review'
        body = 'Test review content'
        created_at = timezone.now()
        rate = 5
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

        review.title = title
        review.body = body
        review.created_at = created_at
        review.rate = rate
        review.author = user
        review.airport = airport
        review.save()

        saved_review = Review.objects.all()
        actual_review = saved_review[0]

        self.assertEqual(actual_review.title, title)
        self.assertEqual(actual_review.body, body)
        self.assertEqual(actual_review.rate, rate)
        self.assertEqual(actual_review.airport, airport)
        self.assertEqual(actual_review.author, user)
