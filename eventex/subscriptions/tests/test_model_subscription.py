from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Junior Indart',
            cpf='1234567890',
            email='juniorindart@hotmail.com',
            phone='67077249814'
        )
        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """Subscription must have an auto created_at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)