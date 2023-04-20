# Generated by Django 3.2.18 on 2023-04-20 09:35

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_alter_articlepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed_video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a URL from Microsoft Stream or Youtube. Please use the page URL rather than the URL from the embed code.'))], help_text='Embed a video')), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('r', 'R'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text=''))], blank=True, null=True, use_json_field=True),
        ),
    ]
