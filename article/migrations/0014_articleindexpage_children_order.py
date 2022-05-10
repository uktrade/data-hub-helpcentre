# Generated by Django 3.2.13 on 2022-05-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_articlepage_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleindexpage',
            name='children_order',
            field=models.CharField(choices=[('-date', 'Date most recent first'), ('sequence', 'Sequence')], default='-date', max_length=150),
        ),
    ]