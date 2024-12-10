from django.shortcuts import render, redirect
from .models import ToDo
# Create your views here.

def todo_list(request):
    tasklist = ToDo.objects.all()
    return render(request, 'todo/index.html', {"tasks": tasklist})

def add_task(request):
    if request.method=='POST':
        title = request.POST.get('title')
        task = request.POST.get('task')
        ToDo.objects.create(title=title, task=task)
    return redirect('Home')