# Generated by Django 2.2.5 on 2023-07-11 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20230711_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 17, 20, 33, 514986)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 17, 20, 33, 514986)),
        ),
    ]
