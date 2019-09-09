# Generated by Django 2.0.5 on 2018-07-01 16:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0008_expertiseclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='prices',
            field=wagtail.core.fields.StreamField([('prices', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('plan', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock()), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StreamBlock([('feature', wagtail.core.blocks.CharBlock()), ('icon', wagtail.core.blocks.CharBlock(help_text='Icons must be a UNCODE character'))], label='Feature'))), ('cost', wagtail.core.blocks.IntegerBlock()), ('hire_button', wagtail.snippets.blocks.SnippetChooserBlock('core.Button'))], label='plan')))]))], blank=True),
        ),
    ]