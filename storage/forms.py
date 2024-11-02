from django import forms
from .models import Folder, File, SharedFile

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class FolderForm(BootstrapFormMixin, forms.ModelForm):
    updated_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = Folder
        fields = ['name', 'parent']

class FileForm(BootstrapFormMixin, forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    updated_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = File
        fields = ['name', 'folder', 'file']

class SharedFileForm(BootstrapFormMixin, forms.ModelForm):
    shared_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = SharedFile
        fields = ['file', 'shared_with', 'permission']
