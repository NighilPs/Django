# Generated by Django 3.1.3 on 2021-01-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210119_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
