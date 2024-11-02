from django.urls import path
from .views import (
    TransactionListCreateView, 
    TransactionDetailView, 
    InvoiceListCreateView, 
    InvoiceDetailView
)

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]
