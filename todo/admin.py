from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'content']}),
    ]

    list_display = ['title', 'content', 'timestamp', 'updated']
    list_filter = ['updated']

admin.site.register(Todo, TodoAdmin)
