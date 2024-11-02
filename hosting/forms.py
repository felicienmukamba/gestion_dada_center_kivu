from django import forms
from .models import Website, WebPage, HostingPlan, Subscription

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class WebsiteForm(BootstrapFormMixin, forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    updated_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Website
        fields = ['domain_name', 'owner']

class WebPageForm(BootstrapFormMixin, forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    updated_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = WebPage
        fields = ['website', 'title', 'content', 'slug']

class HostingPlanForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = HostingPlan
        fields = ['name', 'description', 'price', 'storage_limit', 'bandwidth_limit']

class SubscriptionForm(BootstrapFormMixin, forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'end_date', 'active']
