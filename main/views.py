from django.shortcuts import render
from .models import TodoList

def listTodo(request):
    tasks = TodoList.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request,'home.html',context)