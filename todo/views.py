from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from todo.models import Todo
from todo.forms import TodoForm

def index(request):
    return render(request, 'todo/index.html', {})


@login_required
def profile(request):
    obj_list = Todo.objects.filter(future_date__isnull=True).order_by('-updated')
    scheduled = Todo.objects.filter(future_date__isnull=False).order_by('-updated')
    context = {
        'todo_list': obj_list,
        'scheduled': scheduled
    }
    print(context)
    return render(request, 'todo/profile.html', context)


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'


@login_required
def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('todo:profile'))
    return render(request, 'todo/create.html', context={'form': form})


@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect(reverse('todo:profile'))
    return render(request, 'todo/update.html', context)


@login_required
def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect(reverse('todo:profile'))
    return render(request, 'todo/delete.html', {'todo': todo})


# class CreateView(View):
#     form = TodoForm
#     template_name = 'todo/create.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('todo:index'))
        
#         return render(request, self.template_name, {'form': form})