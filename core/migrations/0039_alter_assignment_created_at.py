# Generated by Django 3.2.8 on 2021-11-27 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20211127_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 12, 32, 54, 148100, tzinfo=utc)),
        ),
    ]