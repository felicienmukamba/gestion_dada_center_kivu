from django.contrib import admin
from .models import Folder, File, SharedFile

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'owner', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__username', 'created_by__username')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('parent', 'owner', 'created_by')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'owner', 'uploaded_by', 'file_type', 'size', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__username', 'uploaded_by__username', 'folder__name')
    list_filter = ('file_type', 'created_at', 'updated_at')
    raw_id_fields = ('folder', 'owner', 'uploaded_by')

@admin.register(SharedFile)
class SharedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'shared_with', 'permission', 'shared_at')
    search_fields = ('file__name', 'shared_with__username')
    list_filter = ('shared_at', 'permission')
    raw_id_fields = ('file', 'shared_with')
