# Generated by Django 3.1.3 on 2021-01-14 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210114_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patients',
            name='dob',
            field=models.CharField(max_length=30),
        ),
    ]
