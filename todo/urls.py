from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('<int:todo_id>/update/', views.update, name='update'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
]