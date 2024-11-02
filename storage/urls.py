from django.urls import path
from .views import (
    FolderListCreateView,
    FolderDetailView,
    FileListCreateView,
    FileDetailView,
    SharedFileListCreateView
)

urlpatterns = [
    path('folders/', FolderListCreateView.as_view(), name='folder-list'),
    path('folders/<int:pk>/', FolderDetailView.as_view(), name='folder-detail'),
    path('folders/<int:folder_pk>/files/', FileListCreateView.as_view(), name='file-list'),
    path('folders/<int:folder_pk>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('files/<int:file_pk>/shared/', SharedFileListCreateView.as_view(), name='sharedfile-list'),
]
