from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Junior Indart', cpf='12345678901',
                    email='juniorindart@hotmail.com', phone='67077249814')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)


    def test_subscription_email_from(self):
        expect = 'juniorindart@gmail.com'

        self.assertEqual(expect, self.email.from_email)


    def test_subscription_email_to(self):
        expect = ['juniorindart@gmail.com', 'juniorindart@hotmail.com']

        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = [
            'Junior Indart',
            '1234567890',
            'juniorindart@hotmail.com',
            '67077249814',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
