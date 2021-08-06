from django.contrib import admin
from .models import BookModel

@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'contributor')
    list_display_links = ('title',)
    ordering = ('-created_at',)