# Generated by Django 2.0.5 on 2018-07-29 23:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailmenus', '0022_auto_20170913_2125'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('core', '0006_auto_20180723_1858'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('studio', '0026_auto_20180729_2330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MinimalisticApp',
            new_name='AppCover',
        ),
    ]
