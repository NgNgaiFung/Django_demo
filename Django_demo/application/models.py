from django.db import models
from django.forms import DateTimeField, ModelForm
from datetime import datetime

# Create your models here.

class Question(models.Model):
    Question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)


class Answer(models.Model):
    Answer_id = models.AutoField(primary_key=True)
    Stuff_id = models.IntegerField(default=0)
    Name = models.CharField(max_length=200)
    Leave_type_choice = ('S', 'Sick Leave'),('A', 'Annual Leave'),('P', 'Personal Leave')
    Leave_type = models.CharField(default = None, max_length=1, choices=Leave_type_choice)
    Reason = models.CharField(default = None, max_length=1000)
    start = models.DateTimeField(blank=False, default=datetime.now())
    end = models.DateTimeField(blank=False, default=datetime.now())

