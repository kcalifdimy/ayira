# Generated by Django 2.0.5 on 2018-07-23 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0022_auto_20180704_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homecontentitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='homecontentitem',
            name='sort_order',
        ),
    ]
