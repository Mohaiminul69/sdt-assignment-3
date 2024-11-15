from django.shortcuts import render
from task import models


# Create your views here.
def home(request):
    tasks = models.Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})
