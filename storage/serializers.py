from rest_framework import serializers
from .models import Folder, File, SharedFile

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent', 'owner', 'created_by', 'created_at', 'updated_at']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'folder', 'owner', 'uploaded_by', 'file', 'file_type', 'size', 'created_at', 'updated_at']

class SharedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = ['id', 'file', 'shared_with', 'permission', 'shared_at']
