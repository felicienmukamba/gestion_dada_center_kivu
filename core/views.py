from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from storage.models import File, Folder, SharedFile
from support.models import SupportTicket

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        tickets = SupportTicket.objects.all()
        folders = Folder.objects.all()
        files = File.objects.all()
        shared_files = SharedFile.objects.all()
        return render(request, 'core/dashbord.html', {
            'users': users,
            'tickets': tickets,
            'folders': folders,
            'files': files,
            'shared_files': shared_files,
        })


class HomePageView(View):
    def get(self, request):
        return render(request, 'core/home.html')