from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Website, WebPage, HostingPlan, Subscription
from .serializers import WebsiteSerializer, WebPageSerializer, HostingPlanSerializer, SubscriptionSerializer

class WebsiteListCreateView(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Website.objects.filter(owner=self.request.user)

class WebsiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Website.objects.filter(owner=self.request.user)

class WebPageListCreateView(generics.ListCreateAPIView):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        website = get_object_or_404(Website, id=self.request.data.get('website_id'), owner=self.request.user)
        serializer.save(website=website)

    def get_queryset(self):
        return WebPage.objects.filter(website__owner=self.request.user)

class WebPageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WebPage.objects.filter(website__owner=self.request.user)

class HostingPlanListCreateView(generics.ListCreateAPIView):
    queryset = HostingPlan.objects.all()
    serializer_class = HostingPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class HostingPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostingPlan.objects.all()
    serializer_class = HostingPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        plan = get_object_or_404(HostingPlan, id=self.request.data.get('plan_id'))
        serializer.save(user=self.request.user, plan=plan)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
