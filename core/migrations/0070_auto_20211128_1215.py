# Generated by Django 3.2.8 on 2021-11-28 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20211128_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='marks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 12, 15, 9, 876515, tzinfo=utc)),
        ),
    ]