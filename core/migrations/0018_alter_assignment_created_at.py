# Generated by Django 3.2.8 on 2021-11-26 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20211126_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 17, 43, 50, 615100, tzinfo=utc)),
        ),
    ]
