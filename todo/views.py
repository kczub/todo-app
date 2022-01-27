from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from todo.models import Todo
from todo.forms import TodoForm

def index(request):
    todos = Todo.objects.order_by('-updated')
    return render(request, 'todo/index.html', {'todos': todos,})

def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/create.html', context={'form': form})

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/detail.html', {'todo': todo})


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.content = request.POST['content']
        todo.save()
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/update.html', {'todo': todo})

def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/delete.html', {'todo': todo})