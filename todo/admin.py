from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'title', 'slug', 'content', 'future_date', 'completed']}),
    ]

    list_display = ['user', 'title', 'content', 'timestamp', 'future_date', 'completed']
    list_filter = ['timestamp']

admin.site.register(Todo, TodoAdmin)
