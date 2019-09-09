# Generated by Django 2.0.8 on 2018-08-12 16:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0027_auto_20180729_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertise',
            name='services',
            field=wagtail.core.fields.StreamField([('services', wagtail.core.blocks.StructBlock([('service', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('portfolio', wagtail.core.blocks.StructBlock([('cover_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock('craftbox.CraftPost'))]))]))], blank=True),
        ),
    ]
