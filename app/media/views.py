"""
Views for the Media API.
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    mixins,
    status,
)

from core.models import (
    MediaType,
    Locale,
    BasicMedia
)

from . import serializers

class BaseModelViewSet(viewsets.ModelViewSet):
    """Base viewset for the models"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class MediaTypeViewSet(BaseModelViewSet):
    """Viewset for the media type request."""
    serializer_class = serializers.MediaTypeSerializer
    queryset = MediaType.objects.all()


class LocaleViewSet(BaseModelViewSet):
    """Viewset for the media type request."""
    serializer_class = serializers.LocaleSerializer
    queryset = Locale.objects.all()


class BasicMediaViewSet(BaseModelViewSet):
    """Viewset for the media type request."""
    serializer_class = serializers.BasicMediaSerializer
    queryset = BasicMedia.objects.all()
