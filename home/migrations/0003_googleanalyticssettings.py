# Generated by Django 2.2.4 on 2019-08-22 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoogleAnalyticsSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "tracking_code",
                    models.CharField(help_text="Your GA tracking code", max_length=50),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        help_text="When checked the GA tracking code will appear on all frontend pages"
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Google Analytics",
            },
        ),
    ]
