# Generated by Django 2.0.5 on 2018-07-18 03:51

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('craftbox', '0009_auto_20180717_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='page',
        ),
        migrations.AddField(
            model_name='craftpost',
            name='post_category',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='craftbox.PostCategory'),
        ),
    ]
