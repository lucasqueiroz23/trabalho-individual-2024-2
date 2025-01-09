# Generated by Django 5.1.2 on 2025-01-09 02:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ratings", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="rated_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_ratings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Rated User",
            ),
        ),
        migrations.AddField(
            model_name="rating",
            name="rating_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="given_ratings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Rating User",
            ),
        ),
    ]
