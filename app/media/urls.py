"""
URL mapping for the media app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from media import views


router = DefaultRouter()
router.register('mediatypes', views.MediaTypeViewSet)
router.register('locales', views.LocaleViewSet)
router.register('basicmedia', views.BasicMediaViewSet)

app_name = 'media'

urlpatterns = [
    path('', include(router.urls)),
]
