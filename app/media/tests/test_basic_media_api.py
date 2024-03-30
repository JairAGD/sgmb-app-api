"""
Test for the media type API.
"""
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import (
    MediaType,
    Locale,
    BasicMedia
)

from media.serializers import BasicMediaSerializer


BASIC_MEDIA_URL = reverse('media:basicmedia-list')


class BasicMediaPublicApiTests(TestCase):
    """Test public request to the media type API."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_basic_media(self):
        """Test retrieving list of basic media anonymously."""
        basic_media1 = MediaType.objects.create(name='Mesa')
        basic_media2 = MediaType.objects.create(name='Silla')

        res = self.client.get(BASIC_MEDIA_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_create_basic_media(self):
        """Test unauthenticathed create basic media results in error."""
        payload = {}
        res = self.client.post(BASIC_MEDIA_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class BasicMediaPrivateApiTests(TestCase):
    """Test for authenticated Media Type API requests."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123')
        self.client=APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieving_basic_media_list(self):
        """Test retrieving list of media type."""
        basic_media1 = BasicMedia.objects.create()
        basic_media2 = BasicMedia.objects.create()

        res = self.client.get(BASIC_MEDIA_URL)

        basicmedias = BasicMedia.objects.all().order_by('id')
        serializer = BasicMediaSerializer(basicmedias, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
