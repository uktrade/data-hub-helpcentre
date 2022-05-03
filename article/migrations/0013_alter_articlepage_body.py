# Generated by Django 3.2.13 on 2022-04-29 11:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20210420_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('r', 'R'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('embed_video', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a URL from Microsoft Stream or Youtube. Please use the page URL rather than the URL from the embed code.'))], help_text='Embed a video'))], blank=True, null=True),
        ),
    ]
