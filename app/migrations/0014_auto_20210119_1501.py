# Generated by Django 3.1.3 on 2021-01-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210119_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.DateField(default=False),
        ),
    ]
