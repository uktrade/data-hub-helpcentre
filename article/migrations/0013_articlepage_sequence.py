# Generated by Django 3.2.13 on 2022-05-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20210420_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
    ]
