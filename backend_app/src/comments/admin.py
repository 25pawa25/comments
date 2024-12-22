from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'created_dt', 'parent', 'is_deleted']
    list_filter = ['is_deleted']
    search_fields = ['author_name', 'text']
    ordering = ['created_dt']