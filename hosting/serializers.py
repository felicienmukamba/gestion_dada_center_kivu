from rest_framework import serializers
from .models import Website, WebPage, HostingPlan, Subscription

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'domain_name', 'owner', 'created_at', 'updated_at']

class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = ['id', 'website', 'title', 'content', 'slug', 'created_at', 'updated_at']

class HostingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostingPlan
        fields = ['id', 'name', 'description', 'price', 'storage_limit', 'bandwidth_limit']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'start_date', 'end_date', 'active']
