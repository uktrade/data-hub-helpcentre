# Generated by Django 2.2.10 on 2020-03-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190822_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='show_recent_child_articles',
            field=models.BooleanField(default=False, help_text='When checked this page will display a list of any descendant articles'),
        ),
    ]
