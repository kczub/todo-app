from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'title', 'slug', 'content', 'future_date']}),
    ]

    list_display = ['user', 'title', 'content', 'timestamp', 'future_date']
    list_filter = ['timestamp']

admin.site.register(Todo, TodoAdmin)
