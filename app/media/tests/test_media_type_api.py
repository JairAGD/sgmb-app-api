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
)

from media.serializers import MediaTypeSerializer


MEDIA_TYPE_URL = reverse('media:mediatype-list')


class MediaTypePublicApiTests(TestCase):
    """Test public request to the media type API."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_media_types(self):
        """Test retrieving list of media type anonymously."""
        media_type1 = MediaType.objects.create(name='Mesa')
        media_type2 = MediaType.objects.create(name='Silla')

        res = self.client.get(MEDIA_TYPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_create_media_type(self):
        """Test unauthenticathed create mediatypes results in error."""
        payload = {"name": "Silla"}
        res = self.client.post(MEDIA_TYPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class MediaTypePrivateApiTests(TestCase):
    """Test for authenticated Media Type API requests."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123')
        self.client=APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieving_media_type_list(self):
        """Test retrieving list of media type."""
        media_type1 = MediaType.objects.create(name='Silla')
        media_type2 = MediaType.objects.create(name='Mesa')

        res = self.client.get(MEDIA_TYPE_URL)

        mediatypes = MediaType.objects.all().order_by('-name')
        serializer = MediaTypeSerializer(mediatypes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
