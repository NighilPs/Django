# Generated by Django 3.1.3 on 2021-01-12 08:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=1024)),
                ('image', models.FileField(upload_to='')),
                ('studies', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('date', multiselectfield.db.fields.MultiSelectField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=27)),
            ],
        ),
        migrations.CreateModel(
            name='DocLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=30)),
                ('dpass', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ida', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phn', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('date', models.DateField(max_length=30)),
                ('start', models.TimeField(max_length=30)),
                ('end', models.TimeField(max_length=30)),
                ('sym', models.CharField(max_length=100)),
                ('pres', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phn', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
