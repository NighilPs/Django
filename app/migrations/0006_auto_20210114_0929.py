# Generated by Django 3.1.3 on 2021-01-14 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210114_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comm',
            new_name='comments',
        ),
    ]