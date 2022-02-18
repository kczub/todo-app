from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'title', 'content', 'future_date', 'completed']}),
    ]

    list_display = ['title', 'user', 'timestamp', 'future_date', 'completed']
    list_filter = ['timestamp']
