from django.contrib import admin
from .models import Tasks

# Register your models here.

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','completed','created_at']
    list_filter = ['completed','created_at']
    search_fields = ['title']