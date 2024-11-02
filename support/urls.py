from django.urls import path
from .views import (
    SupportTicketListCreateView,
    SupportTicketDetailView,
    AllSupportTicketsView
)

urlpatterns = [
    path('tickets/', SupportTicketListCreateView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', SupportTicketDetailView.as_view(), name='ticket-detail'),
    path('all-tickets/', AllSupportTicketsView.as_view(), name='all-tickets'),
]
