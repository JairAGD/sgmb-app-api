"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import (
    MediaType,
    BasicMedia,
    Locale
)

class ModelTests(TestCase):
    """Test db models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Tests email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_media_type(self):
        """Test creating a Media Type."""
        mediatype = MediaType.objects.create(name='Mesa')

        self.assertEqual(str(mediatype), mediatype.name)

    def test_create_locale(self):
        """Test creating a Locale."""
        locale = Locale.objects.create(name='Lab1')

        self.assertEqual(str(locale), locale.name)

    def test_create_basic_media(self):
        """Test creating basic media."""
        bm = BasicMedia.objects.create()

        self.assertEqual(str(bm), f'MB: {bm.id}')
        self.assertIsInstance(bm, BasicMedia)
