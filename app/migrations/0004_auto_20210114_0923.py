# Generated by Django 3.1.3 on 2021-01-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210114_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
