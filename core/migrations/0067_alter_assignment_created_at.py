# Generated by Django 3.2.8 on 2021-11-28 06:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20211127_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 6, 34, 50, 764117, tzinfo=utc)),
        ),
    ]