from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todo.models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos,})

def create(request):
    if request.method == 'POST':
        content = request.POST['content']
        Todo.objects.create(content=content)
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/create.html')

def update(request):
    return render(request, 'todo/update.html')

# def delete(request):
#     return render(request, 'todo/')
