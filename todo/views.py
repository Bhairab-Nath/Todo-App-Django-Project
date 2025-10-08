from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo.models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')
