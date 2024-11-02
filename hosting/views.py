from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Website, WebPage, HostingPlan, Subscription
from .forms import WebsiteForm, WebPageForm, HostingPlanForm, SubscriptionForm

class WebsiteListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        websites = Website.objects.filter(owner=request.user)
        form = WebsiteForm()
        return render(request, 'websites/website_list.html', {'websites': websites, 'form': form})

    def post(self, request):
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.owner = request.user
            website.save()
            return redirect('website-list')
        websites = Website.objects.filter(owner=request.user)
        return render(request, 'websites/website_list.html', {'websites': websites, 'form': form})

class WebsiteDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        website = get_object_or_404(Website, pk=pk, owner=request.user)
        return render(request, 'websites/website_detail.html', {'website': website})

    def post(self, request, pk):
        website = get_object_or_404(Website, pk=pk, owner=request.user)
        if 'edit' in request.POST:
            form = WebsiteForm(request.POST, instance=website)
            if form.is_valid():
                form.save()
                return redirect('website-detail', pk=pk)
        elif 'delete' in request.POST:
            website.delete()
            return redirect('website-list')
        return redirect('website-detail', pk=pk)

class WebPageListCreateView(LoginRequiredMixin, View):
    def get(self, request, website_pk):
        website = get_object_or_404(Website, pk=website_pk, owner=request.user)
        pages = website.pages.all()
        form = WebPageForm()
        return render(request, 'webpages/webpage_list.html', {'website': website, 'pages': pages, 'form': form})

    def post(self, request, website_pk):
        website = get_object_or_404(Website, pk=website_pk, owner=request.user)
        form = WebPageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.website = website
            page.save()
            return redirect('webpage-list', website_pk=website.pk)
        pages = website.pages.all()
        return render(request, 'webpages/webpage_list.html', {'website': website, 'pages': pages, 'form': form})

class WebPageDetailView(LoginRequiredMixin, View):
    def get(self, request, website_pk, pk):
        website = get_object_or_404(Website, pk=website_pk, owner=request.user)
        page = get_object_or_404(WebPage, pk=pk, website=website)
        return render(request, 'webpages/webpage_detail.html', {'website': website, 'page': page})

    def post(self, request, website_pk, pk):
        website = get_object_or_404(Website, pk=website_pk, owner=request.user)
        page = get_object_or_404(WebPage, pk=pk, website=website)
        if 'edit' in request.POST:
            form = WebPageForm(request.POST, instance=page)
            if form.is_valid():
                form.save()
                return redirect('webpage-detail', website_pk=website.pk, pk=pk)
        elif 'delete' in request.POST:
            page.delete()
            return redirect('webpage-list', website_pk=website.pk)
        return redirect('webpage-detail', website_pk=website.pk, pk=pk)

class HostingPlanListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        plans = HostingPlan.objects.all()
        form = HostingPlanForm()
        return render(request, 'hostingplans/hostingplan_list.html', {'plans': plans, 'form': form})

    def post(self, request):
        form = HostingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostingplan-list')
        plans = HostingPlan.objects.all()
        return render(request, 'hostingplans/hostingplan_list.html', {'plans': plans, 'form': form})

class SubscriptionListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        form = SubscriptionForm()
        return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions, 'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('subscription-list')
        subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions, 'form': form})

class SubscriptionDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk, user=request.user)
        return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})

    def post(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk, user=request.user)
        if 'edit' in request.POST:
            form = SubscriptionForm(request.POST, instance=subscription)
            if form.is_valid():
                form.save()
                return redirect('subscription-detail', pk=pk)
        elif 'delete' in request.POST:
            subscription.delete()
            return redirect('subscription-list')
        return redirect('subscription-detail', pk=pk)
