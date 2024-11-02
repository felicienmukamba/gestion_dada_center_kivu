from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm
from django.contrib.auth.models import User

class UserRegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                print(f"User {user.username} created successfully")  # Log user creation
                # Verify user is a User instance
                if isinstance(user, User):
                    profile, created = UserProfile.objects.get_or_create(user=user)
                    if created:
                        print(f"UserProfile for {user.username} created successfully")
                    login(request, user)
                    return redirect('profile', pk=user.pk)
                else:
                    print(f"User creation failed: {user} is not a User instance")
            else:
                print("User creation failed")
        else:
            print("Form is not valid")
            print(form.errors)
        return render(request, 'users/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and isinstance(user, CustomUser):
                # Check and create user profile if it doesn't exist
                profile, created = UserProfile.objects.get_or_create(user=user)
                if created:
                    print(f"UserProfile for {user.username} created successfully during login")
                login(request, user)
                return redirect('profile', pk=user.pk)
            else:
                form.add_error(None, "Invalid username or password")
        else:
            print("Login form is not valid")
        return render(request, 'users/login.html', {'form': form, 'errors': form.errors})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class UserListView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('profile', pk=request.user.pk)
        users = CustomUser.objects.all()
        return render(request, 'users/user_list.html', {'users': users})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if request.user != user:
            return redirect('profile', pk=request.user.pk)
        user_form = CustomUserChangeForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)
        return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if request.user != user:
            return redirect('profile', pk=request.user.pk)
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', pk=user.pk)
        return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})