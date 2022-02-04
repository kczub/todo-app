from django.urls import path

from todo.views import index, ProfileView, DetailView, create, update, delete

app_name = 'todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('create/', create, name='create'),
    path('<int:todo_id>/update/', update, name='update'),
    path('<int:todo_id>/delete/', delete, name='delete'),
    path('profile/', ProfileView.as_view(), name='profile')
]