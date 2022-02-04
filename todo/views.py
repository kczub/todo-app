from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View

from todo.models import Todo
from todo.forms import TodoForm

def index(request):
    return render(request, 'todo/index.html', {})


class ProfileView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'todo/profile.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-updated')

    
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