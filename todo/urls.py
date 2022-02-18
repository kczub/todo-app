from django.urls import path

from .views import (
    index_view,
    profile_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
    confirm_completed_view,
    completed_view
)


app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    path('create/', create_view, name='create'),
    path('completed/', completed_view, name='completed'),
    path('profile/', profile_view, name='profile'),
    path('<int:pk>/confirm-complete/', confirm_completed_view, name='confirm_completed'),
    path('<int:pk>/confirm-delete/', delete_view, name='delete'),
    path('<int:pk>/', detail_view, name='detail'),
    path('<int:pk>/update/', update_view, name='update'),
]