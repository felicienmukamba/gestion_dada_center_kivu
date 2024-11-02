from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

def validate_file_type(file):
    valid_mime_types = [
        'image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp', 'image/tiff', 'image/svg+xml',
        'application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/rtf', 'text/plain', 'text/csv',
        'video/mp4', 'video/x-msvideo', 'video/x-ms-wmv', 'video/quicktime', 'video/mpeg',
        'audio/mpeg', 'audio/wav', 'audio/ogg',
        'application/zip', 'application/x-tar', 'application/x-gzip', 'application/x-rar-compressed'
    ]
    file_type = file.file.content_type
    if file_type not in valid_mime_types:
        raise ValidationError(f'Unsupported file type: {file_type}')

def file_upload_to(instance, filename):
    file_type_category = instance.file.file.content_type.split('/')[0]
    return f'{file_type_category}_files/{filename}'

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subfolders', null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_folders')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='created_folders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_files')
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='uploaded_files')
    file = models.FileField(upload_to=file_upload_to, validators=[validate_file_type])
    file_type = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.file_type = self.file.file.content_type
        self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SharedFile(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='shared_with')
    shared_with = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='shared_files')
    permission = models.CharField(max_length=10, choices=[('read', 'Read'), ('write', 'Write')], default='read')
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} shared with {self.shared_with.username}"
