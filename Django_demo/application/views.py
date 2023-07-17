from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import QuestionForm, AnswerForm

# Create your views here.

def test(requset):
    return HttpResponse("Hello World!")

def home(request):
    return render(request, "home.html")

def application(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("application")
    else:
        form = AnswerForm()
    return render(request,"application/application.html",{"form":form})