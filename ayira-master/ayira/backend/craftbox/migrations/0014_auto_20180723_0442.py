# Generated by Django 2.0.5 on 2018-07-23 04:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('craftbox', '0013_crafthome_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crafthome',
            old_name='description',
            new_name='header',
        ),
        migrations.AlterField(
            model_name='craftpost',
            name='body',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.RichTextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(template='frontend/craftbox/blocks/image.html')), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', label='Language')), ('code', wagtail.core.blocks.TextBlock(label='Code'))]))]),
        ),
    ]
