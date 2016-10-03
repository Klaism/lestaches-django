from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm

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

def viewTask(request, name):
    task = Task.objects.get(name = name)
    return render(request,'lesTaches/task.html',{"task":task})


def newTask(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
        return render(request,'lesTaches/forms/task.html',{"form":form})


def editTask(request,name):

    task = Task.objects.get(name = name)

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm(instance=task)
        return render(request,'lesTaches/forms/task.html',{"form":form})


def deleteTask(request, name):
    task = Task.objects.filter(name = name)
    task.delete()
    return HttpResponseRedirect(reverse('task_list'))
