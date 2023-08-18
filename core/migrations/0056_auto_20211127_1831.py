# Generated by Django 3.2.8 on 2021-11-27 18:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_alter_assignment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='assignment_name',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='university_id',
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='Assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.assignment'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 18, 31, 47, 249462, tzinfo=utc)),
        ),
    ]
