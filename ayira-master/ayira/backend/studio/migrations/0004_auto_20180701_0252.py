# Generated by Django 2.0.5 on 2018-07-01 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_auto_20180701_0240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'about page'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='process',
            new_name='body',
        ),
    ]