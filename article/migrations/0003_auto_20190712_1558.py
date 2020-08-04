# Generated by Django 2.2.3 on 2019-07-12 15:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_auto_20190712_1537"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
