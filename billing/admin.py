from django.contrib import admin
from .models import Transaction, Invoice

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'description')
    search_fields = ('user__username', 'amount', 'date')
    list_filter = ('date', 'amount')
    raw_id_fields = ('user',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total', 'paid')
    search_fields = ('user__username', 'date', 'total')
    list_filter = ('date', 'paid')
    raw_id_fields = ('user',)
