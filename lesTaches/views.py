from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request,name):
    if not name:
        name = "toi"
    return HttpResponse("Hello "+name)


def task_listing(request):
     objects = Task.objects.all().order_by('-createdDate')
     return render(request,'lesTaches/list.html', {"taches": objects })
