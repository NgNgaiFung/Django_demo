# Generated by Django 2.2.5 on 2023-07-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='Reason',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='answer',
            name='Stuff_id',
            field=models.IntegerField(default=0),
        ),
    ]
