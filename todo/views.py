from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from todo.models import Todo
from todo.forms import TodoForm

User = settings.AUTH_USER_MODEL


def index_view(request):
    return render(request, 'todo/index.html', {})


@login_required
def profile_view(request):
    user = request.user
    qs = Todo.objects.filter(user__username=user)
    context = {
        'active': qs.filter(completed=False).order_by('-updated'),
        'completed': qs.filter(completed=True)[:3],
    }
    return render(request, 'todo/profile.html', context)


@login_required
def detail_view(request, pk):
    todo_object = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo_object
    }
    return render(request, 'todo/detail.html', context)


@login_required
def create_view(request):
    form = TodoForm(request.POST or None)
    context = {
        'form': form,
        'todo': None
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(reverse('todo:profile'))

    return render(request, 'todo/create-update.html', context)


@login_required
def update_view(request, pk):
    todo_object = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(request.POST or None, instance=todo_object)
    context = {
        'form': form,
        'todo': todo_object
    }
    if form.is_valid():
        form.save()
        return redirect(todo_object)

    return render(request, 'todo/create-update.html', context)


@login_required
def delete_view(request, pk):
    todo_object = get_object_or_404(Todo, pk=pk, user=request.user)
    context = {
        'todo': todo_object
    }
    if request.method == 'POST':
        todo_object.delete()
        return redirect('todo:profile')

    return render(request, 'todo/delete.html', context)


@login_required
def completed_view(request, pk):
    todo_object = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo_object
    }
    if request.method == 'POST':
        todo_object.completed = True
        todo_object.save()
        return redirect('todo:profile')

    return render(request, 'todo/completed.html', context)