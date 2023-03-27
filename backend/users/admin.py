from django.contrib import admin

from .models import User


@admin.register(User)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_filter = ['username', 'email']
