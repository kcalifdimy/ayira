# Generated by Django 2.0.5 on 2018-07-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craftbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='craftpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
