# Generated by Django 2.0.5 on 2018-07-02 14:28

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0015_auto_20180702_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacts',
            field=wagtail.core.fields.StreamField([('contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('info', wagtail.core.blocks.CharBlock()), ('icon', wagtail.images.blocks.ImageChooserBlock()), ('category', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'email'), ('phone', 'phone'), ('address', 'address')]))], label='office contact')))], blank=True),
        ),
    ]