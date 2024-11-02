from django.urls import path
from .views import (
    WebsiteListCreateView, 
    WebsiteDetailView, 
    WebPageListCreateView, 
    WebPageDetailView, 
    HostingPlanListCreateView, 
    SubscriptionListCreateView, 
    SubscriptionDetailView
)

urlpatterns = [
    path('websites/', WebsiteListCreateView.as_view(), name='website-list'),
    path('websites/<int:pk>/', WebsiteDetailView.as_view(), name='website-detail'),
    path('websites/<int:website_pk>/pages/', WebPageListCreateView.as_view(), name='webpage-list'),
    path('websites/<int:website_pk>/pages/<int:pk>/', WebPageDetailView.as_view(), name='webpage-detail'),
    path('hosting-plans/', HostingPlanListCreateView.as_view(), name='hostingplan-list'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
]
