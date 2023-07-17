# Generated by Django 4.1 on 2023-07-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("Answer_id", models.AutoField(primary_key=True, serialize=False)),
                ("Stuff_id", models.IntegerField(max_length=8)),
                ("Name", models.CharField(max_length=200)),
                ("Leave_type", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("Question_id", models.AutoField(primary_key=True, serialize=False)),
                ("question_text", models.CharField(max_length=200)),
            ],
        ),
    ]
