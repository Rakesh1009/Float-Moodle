# Generated by Django 3.2.8 on 2021-11-27 12:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 12, 33, 43, 22727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='assignment_name',
            field=models.CharField(default='uk', max_length=500),
        ),
    ]
