# Generated by Django 3.1.2 on 2020-11-06 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]