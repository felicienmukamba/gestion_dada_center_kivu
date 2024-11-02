from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Folder, File, SharedFile
from .forms import FolderForm, FileForm, SharedFileForm
from django.core.exceptions import PermissionDenied

class FolderListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        folders = Folder.objects.filter(owner=request.user, parent__isnull=True)
        form = FolderForm()
        return render(request, 'folders/folder_list.html', {'folders': folders, 'form': form})

    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.created_by = request.user
            folder.save()
            return redirect('folder-list')
        folders = Folder.objects.filter(owner=request.user, parent__isnull=True)
        return render(request, 'folders/folder_list.html', {'folders': folders, 'form': form})

class FolderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk, owner=request.user)
        subfolders = folder.subfolders.all()
        files = folder.files.all()
        form = FolderForm()
        return render(request, 'folders/folder_detail.html', {'folder': folder, 'subfolders': subfolders, 'files': files, 'form': form})

    def post(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk, owner=request.user)
        if 'edit' in request.POST:
            form = FolderForm(request.POST, instance=folder)
            if form.is_valid():
                form.save()
                return redirect('folder-detail', pk=pk)
        elif 'delete' in request.POST:
            folder.delete()
            return redirect('folder-list')
        return redirect('folder-detail', pk=pk)

class FileListCreateView(LoginRequiredMixin, View):
    def get(self, request, folder_pk):
        folder = get_object_or_404(Folder, pk=folder_pk, owner=request.user)
        files = folder.files.all()
        form = FileForm()
        return render(request, 'files/file_list.html', {'folder': folder, 'files': files, 'form': form})

    def post(self, request, folder_pk):
        folder = get_object_or_404(Folder, pk=folder_pk, owner=request.user)
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder
            file.owner = request.user
            file.uploaded_by = request.user
            file.save()
            return redirect('file-list', folder_pk=folder.pk)
        files = folder.files.all()
        return render(request, 'files/file_list.html', {'folder': folder, 'files': files, 'form': form})

class FileDetailView(LoginRequiredMixin, View):
    def get(self, request, folder_pk, pk):
        folder = get_object_or_404(Folder, pk=folder_pk, owner=request.user)
        file = get_object_or_404(File, pk=pk, folder=folder)
        return render(request, 'files/file_detail.html', {'folder': folder, 'file': file})

    def post(self, request, folder_pk, pk):
        folder = get_object_or_404(Folder, pk=folder_pk, owner=request.user)
        file = get_object_or_404(File, pk=pk, folder=folder)
        if 'edit' in request.POST:
            form = FileForm(request.POST, request.FILES, instance=file)
            if form.is_valid():
                form.save()
                return redirect('file-detail', folder_pk=folder.pk, pk=pk)
        elif 'delete' in request.POST:
            file.delete()
            return redirect('file-list', folder_pk=folder.pk)
        return redirect('file-detail', folder_pk=folder.pk, pk=pk)

class SharedFileListCreateView(LoginRequiredMixin, View):
    def get(self, request, file_pk):
        file = get_object_or_404(File, pk=file_pk, owner=request.user)
        shared_files = file.shared_with.all()
        form = SharedFileForm()
        return render(request, 'sharedfiles/sharedfile_list.html', {'file': file, 'shared_files': shared_files, 'form': form})

    def post(self, request, file_pk):
        file = get_object_or_404(File, pk=file_pk, owner=request.user)
        form = SharedFileForm(request.POST)
        if form.is_valid():
            shared_file = form.save(commit=False)
            shared_file.file = file
            shared_file.save()
            return redirect('sharedfile-list', file_pk=file.pk)
        shared_files = file.shared_with.all()
        return render(request, 'sharedfiles/sharedfile_list.html', {'file': file, 'shared_files': shared_files, 'form': form})
