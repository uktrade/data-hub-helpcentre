# Generated by Django 2.2.3 on 2019-07-12 15:35

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ArticlePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("date", models.DateField(verbose_name="Post date")),
                ("intro", models.CharField(max_length=250)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", wagtail.blocks.CharBlock(classname="full title")),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
