from django.contrib import admin

from .models import Note


@admin.register(Note)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'author', 'pub_date']
    list_filter = ['author', 'pub_date']
    exclude = ('soundex',)
