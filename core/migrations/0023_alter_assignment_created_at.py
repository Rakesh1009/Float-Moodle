# Generated by Django 3.2.8 on 2021-11-27 08:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 8, 3, 56, 957738, tzinfo=utc)),
        ),
    ]
