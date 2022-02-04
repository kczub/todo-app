from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'content', 'future_date']}),
    ]

    list_display = ['title', 'content', 'timestamp', 'future_date']
    list_filter = ['timestamp']

admin.site.register(Todo, TodoAdmin)
