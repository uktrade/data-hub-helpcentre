# Generated by Django 2.2.9 on 2020-02-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0009_articlehomepage_show_recent_child_articles"),
    ]

    operations = [
        migrations.AddField(
            model_name="articleindexpage",
            name="show_in_columns",
            field=models.BooleanField(
                default=True,
                help_text="When set to True, any child articles will be displayed in columns, otherwise full width",
            ),
        ),
        migrations.AlterField(
            model_name="articlehomepage",
            name="show_recent_child_articles",
            field=models.BooleanField(
                default=True,
                help_text="When checked this page will display a list of any descendant articles",
            ),
        ),
    ]
