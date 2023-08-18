# Generated by Django 3.2.8 on 2021-11-27 20:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20211127_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='Course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 20, 25, 38, 607194, tzinfo=utc)),
        ),
    ]
