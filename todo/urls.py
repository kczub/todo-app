from django.urls import path

from .views import (
    index_view,
    profile_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
    completed_view
)


app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    path('create/', create_view, name='create'),
    path('profile/', profile_view, name='profile'),
    path('<int:pk>/completed/', completed_view, name='completed'),
    path('<int:pk>/delete/', delete_view, name='delete'),
    path('<int:pk>/', detail_view, name='detail'),
    path('<int:pk>/update/', update_view, name='update'),
]