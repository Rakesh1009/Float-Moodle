# Generated by Django 3.2.8 on 2021-11-27 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 8, 0, 12, 186701, tzinfo=utc)),
        ),
    ]
