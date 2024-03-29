# Generated by Django 2.2.4 on 2019-08-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_googleanalyticssettings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="googleanalyticssettings",
            name="is_enabled",
            field=models.BooleanField(
                default=False,
                help_text="When checked the GA tracking code will appear on all frontend pages",
            ),
        ),
    ]
