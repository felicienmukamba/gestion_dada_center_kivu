from django import forms
from .models import Transaction, Invoice

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class TransactionForm(BootstrapFormMixin, forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'description']

class InvoiceForm(BootstrapFormMixin, forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Invoice
        fields = ['user', 'total', 'paid']
