# Generated by Django 3.2.8 on 2021-11-27 12:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmission',
            name='university_id',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 12, 52, 12, 893331, tzinfo=utc)),
        ),
    ]
