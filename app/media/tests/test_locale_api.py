"""
Test for the locale API.
"""
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import (
    Locale,
)

from media.serializers import LocaleSerializer


LOCALES_URL = reverse('media:locale-list')


class LocalePublicApiTests(TestCase):
    """Test public request to the locale API."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_locales(self):
        """Test retrieving list of locales anonymously."""
        locale1 = Locale.objects.create(name='Lab2')
        locale2 = Locale.objects.create(name='Lab1')

        res = self.client.get(LOCALES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_create_locale(self):
        """Test unauthenticathed create locales results in error."""
        payload = {"name": "Lab1"}
        res = self.client.post(LOCALES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class LocalePrivateApiTests(TestCase):
    """Test for authenticated locale API requests."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123')
        self.client=APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieving_locale_list(self):
        """Test retrieving list of locale."""
        locale1 = Locale.objects.create(name='Lab1')
        locale2 = Locale.objects.create(name='Lab2')

        res = self.client.get(LOCALES_URL)

        locales = Locale.objects.all()
        serializer = LocaleSerializer(locales, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
