# Generated by Django 2.2.3 on 2019-07-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0003_auto_20190712_1558"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="intro",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
