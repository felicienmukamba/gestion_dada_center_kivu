from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Invoice
from .forms import TransactionForm, InvoiceForm

class TransactionListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        form = TransactionForm()
        return render(request, 'transactions/transaction_list.html', {'transactions': transactions, 'form': form})

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction-list')
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'transactions/transaction_list.html', {'transactions': transactions, 'form': form})

class TransactionDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        if 'edit' in request.POST:
            form = TransactionForm(request.POST, instance=transaction)
            if form.is_valid():
                form.save()
                return redirect('transaction-detail', pk=pk)
        elif 'delete' in request.POST:
            transaction.delete()
            return redirect('transaction-list')
        return redirect('transaction-detail', pk=pk)

class InvoiceListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        invoices = Invoice.objects.filter(user=request.user)
        form = InvoiceForm()
        return render(request, 'invoices/invoice_list.html', {'invoices': invoices, 'form': form})

    def post(self, request):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
            return redirect('invoice-list')
        invoices = Invoice.objects.filter(user=request.user)
        return render(request, 'invoices/invoice_list.html', {'invoices': invoices, 'form': form})

class InvoiceDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk, user=request.user)
        return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})

    def post(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk, user=request.user)
        if 'edit' in request.POST:
            form = InvoiceForm(request.POST, instance=invoice)
            if form.is_valid():
                form.save()
                return redirect('invoice-detail', pk=pk)
        elif 'delete' in request.POST:
            invoice.delete()
            return redirect('invoice-list')
        return redirect('invoice-detail', pk=pk)
