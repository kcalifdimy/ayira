# Generated by Django 2.0.5 on 2018-07-01 16:29

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0010_expertise_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertise',
            name='prices',
            field=wagtail.core.fields.StreamField([('prices', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('plan', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock()), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('feature', wagtail.core.blocks.CharBlock()), ('icon', wagtail.core.blocks.CharBlock(help_text='Icons must be a UNCODE character'))], label='Feature'))), ('cost', wagtail.core.blocks.IntegerBlock()), ('hire_button', wagtail.snippets.blocks.SnippetChooserBlock('core.Button'))], label='plan')))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='services',
            field=wagtail.core.fields.StreamField([('services', wagtail.core.blocks.StructBlock([('service', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('summary', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('case_study', wagtail.core.blocks.StructBlock([('cover_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock('craftbox.CraftPost'))]))])))]))], blank=True),
        ),
    ]