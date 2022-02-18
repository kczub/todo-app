from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from todo.models import Todo
from todo.forms import TodoForm


User = settings.AUTH_USER_MODEL

def index(request):
    return render(request, 'todo/index.html', {})


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'todo/profile.html'

    def get_queryset(self):
        user = self.request.user.get_username()
        queryset = Todo.objects.filter(user__username=user)
        data = {
            'todo': queryset.filter(completed=False).order_by('-updated'),
            'completed': queryset.filter(completed=True)[:3],
            'no_date': queryset.filter(future_date__isnull=True).order_by('-updated'),
            'scheduled': queryset.filter(future_date__isnull=False).order_by('-updated'),
        }
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context.get('object_list')


class DetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/detail.html'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create-update.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(obj=self.object)

    def form_valid(self, form=form_class):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            return redirect(reverse('todo:profile'))


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create-update.html'
    

class TodoDeleteView(LoginRequiredMixin, DeleteView): 
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:profile')

def todo_completed_view(request, pk):
    todo_object = get_object_or_404(Todo, pk=pk)
    context = {'object': todo_object}
    if request.method == 'POST':
        todo_object.completed = True
        todo_object.save()
        return redirect('todo:profile')
    return render(request, 'todo/completed.html', context)