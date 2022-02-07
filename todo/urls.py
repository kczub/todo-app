from django.urls import path

from todo.views import index, ProfileView, DetailView, TodoCreateView, TodoUpdateView, TodoDeleteView


app_name = 'todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
    path('profile/', ProfileView.as_view(), name='profile')
]