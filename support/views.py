from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import SupportTicket
from .forms import SupportTicketForm

class SupportTicketListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        tickets = SupportTicket.objects.filter(user=request.user)
        form = SupportTicketForm()
        return render(request, 'support_tickets/ticket_list.html', {'tickets': tickets, 'form': form})

    def post(self, request):
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket-list')
        tickets = SupportTicket.objects.filter(user=request.user)
        return render(request, 'support_tickets/ticket_list.html', {'tickets': tickets, 'form': form})

class SupportTicketDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        ticket = get_object_or_404(SupportTicket, pk=self.kwargs['pk'])
        return self.request.user == ticket.user

    def handle_no_permission(self):
        return redirect('ticket-list')

    def get(self, request, pk):
        ticket = get_object_or_404(SupportTicket, pk=pk, user=request.user)
        return render(request, 'support_tickets/ticket_detail.html', {'ticket': ticket})

    def post(self, request, pk):
        ticket = get_object_or_404(SupportTicket, pk=pk, user=request.user)
        if 'edit' in request.POST:
            form = SupportTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket-detail', pk=pk)
        elif 'resolve' in request.POST:
            ticket.resolved = True
            ticket.save()
            return redirect('ticket-list')
        elif 'delete' in request.POST:
            ticket.delete()
            return redirect('ticket-list')
        return redirect('ticket-detail', pk=pk)

class AllSupportTicketsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('ticket-list')

    def get(self, request):
        tickets = SupportTicket.objects.all()
        return render(request, 'support_tickets/all_tickets.html', {'tickets': tickets})
