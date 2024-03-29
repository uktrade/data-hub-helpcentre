# Generated by Django 2.2.4 on 2019-08-06 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0006_articlepage_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="author",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose from the list or create a new user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="authored_pages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
