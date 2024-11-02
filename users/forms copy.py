from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'phone_number', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'phone_number', 'is_active', 'is_staff']

class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    twitter_handle = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_profile = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'website', 'twitter_handle', 'linkedin_profile']
