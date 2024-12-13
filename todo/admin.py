from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'title', 'due_date', 'status']
    list_filter = ['status', 'due_date']
    search_fields = ['title', 'description', 'tags']
    readonly_fields = ['timestamp']
