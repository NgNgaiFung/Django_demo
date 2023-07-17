from django.db import models
from django.forms import ModelForm
from .models import Question, Answer
from django import forms

######################################


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
        widgets = {
            "start": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "Leave_type": forms.RadioSelect,
        }