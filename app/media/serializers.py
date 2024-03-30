"""
Serializers for the Media API request.
"""
from rest_framework import serializers

from user.serializers import UserSerializer
from core.models import (
    MediaType,
    Locale,
    BasicMedia
)


class MediaTypeSerializer(serializers.ModelSerializer):
    """Serializer for the media types."""

    class Meta:
        model = MediaType
        fields = ['id', 'name']
        read_only_fields = ['id']


class LocaleSerializer(serializers.ModelSerializer):
    """Serializer for the locale object."""
    responsible = UserSerializer(many=False, required=False)

    class Meta:
        model = Locale
        fields = ['id', 'name', 'responsible']
        read_only_field = ['id']


class BasicMediaSerializer(serializers.ModelSerializer):
    """Serializer for the Basic Media."""
    type = serializers.PrimaryKeyRelatedField(many=False,
                                              queryset=MediaType.objects.all(),
                                              required=False)
    locale = serializers.PrimaryKeyRelatedField(many=False,
                                                queryset=Locale.objects.all(),
                                                required=False)

    class Meta:
        model = BasicMedia
        fields = ['id', 'type', 'locale']
        read_only_fields = ['id']
        extra_kwargs = {'type': {'allow_null': True,
                                 'allow_blank': True},
                        'locale': {'allow_null': True,
                                   'allow_blank': True}}
