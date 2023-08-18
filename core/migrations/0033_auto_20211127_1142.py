# Generated by Django 3.2.8 on 2021-11-27 11:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20211127_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='feedback',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 11, 42, 26, 808209, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200)),
                ('AssignmentSubmission', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.assignmentsubmission')),
            ],
        ),
    ]
