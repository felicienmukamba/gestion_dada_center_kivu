from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Folder, File, SharedFile
from .serializers import FolderSerializer, FileSerializer, SharedFileSerializer
from django.contrib.auth import get_user_model

class FolderListCreateView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, created_by=self.request.user)

    def get_queryset(self):
        return Folder.objects.filter(owner=self.request.user)

class FolderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Folder.objects.filter(owner=self.request.user)

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        folder = get_object_or_404(Folder, id=self.request.data.get('folder_id'), owner=self.request.user)
        serializer.save(folder=folder, owner=self.request.user, uploaded_by=self.request.user)

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

class ShareFileView(generics.GenericAPIView):
    serializer_class = SharedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file = get_object_or_404(File, id=request.data.get('file_id'), owner=self.request.user)
        shared_with = get_object_or_404(get_user_model(), id=request.data.get('shared_with_id'))
        permission = request.data.get('permission', 'read')
        shared_file, created = SharedFile.objects.get_or_create(
            file=file,
            shared_with=shared_with,
            defaults={'permission': permission}
        )
        if not created:
            shared_file.permission = permission
            shared_file.save()
        return Response({'status': 'file shared', 'permission': shared_file.permission})

class SharedFileListView(generics.ListAPIView):
    serializer_class = SharedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SharedFile.objects.filter(shared_with=self.request.user)
