# Generated by Django 2.0.5 on 2018-07-23 18:54

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180706_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='moto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
