from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import SupportTicket
from .serializers import SupportTicketSerializer

class SupportTicketListCreateView(generics.ListCreateAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)

class SupportTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)
