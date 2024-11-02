from django.contrib import admin
from .models import Website, WebPage, HostingPlan, Subscription

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('domain_name', 'owner', 'created_at', 'updated_at')
    search_fields = ('domain_name', 'owner__username')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('owner',)

@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'website', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'website__domain_name', 'slug')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('website',)

@admin.register(HostingPlan)
class HostingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'storage_limit', 'bandwidth_limit')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'active')
    search_fields = ('user__username', 'plan__name')
    list_filter = ('start_date', 'end_date', 'active')
    raw_id_fields = ('user', 'plan')
