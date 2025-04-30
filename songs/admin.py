from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'mood', 'language', 'created_at')
    list_filter = ('mood', 'language')
    search_fields = ('title', 'description')
