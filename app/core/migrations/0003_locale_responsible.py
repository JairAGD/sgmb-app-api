# Generated by Django 4.2.11 on 2024-03-30 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_locale_mediatype_basicmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='locale',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
