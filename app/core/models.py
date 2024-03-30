"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for user model."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email!.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create superuser with given details."""
        user = self.model(email=email, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class MediaType(models.Model):
    """Media type of assets."""
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Locale(models.Model):
    """Premises wich a media belogs to."""
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class BasicMedia(models.Model):
    """Basic Media asset."""
    type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, blank=True, null=True)
    locale = models.ForeignKey(Locale, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'MB: {self.id}'
