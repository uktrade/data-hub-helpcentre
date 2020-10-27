import datetime
import json

from django.db import migrations
from django.contrib.auth import get_user_model

from wagtail.core.models import Page


def create_accessibility_page(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    HomePage = apps.get_model('home.HomePage')
    ArticlePage = apps.get_model('article.ArticlePage')

    home_page = HomePage.objects.all().first()

    article_content_type, _ = ContentType.objects.get_or_create(
        model='articlepage', 
        app_label='article',
    )

    parent = Page.objects.filter(slug=home_page.slug).first()

    current_time = datetime.datetime.now() 

    blocks = []

    blocks.append({
        'type': 'paragraph',
        'value': 'TODO - add accessiblity content'
    },)

    body = json.dumps(blocks)

    accessibility_page = ArticlePage(
        content_type=article_content_type,
        date=current_time,
        intro="Accessibility Statement for Data Services Help Centre",
        body=body,
        first_published_at=current_time,
        last_published_at=current_time,
        title="Accessibility Statement",
        slug="accessibility-statement",
        live=True,
    )

    parent.add_child(instance=accessibility_page)
    parent.save()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200206_1524'),
        ('home', '0005_homepage_show_recent_child_articles'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.RunPython(create_accessibility_page),
    ]
