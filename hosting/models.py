from django.db import models
from django.contrib.auth import get_user_model

class Website(models.Model):
    domain_name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain_name

class WebPage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HostingPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage_limit = models.PositiveIntegerField(help_text="Storage limit in MB")
    bandwidth_limit = models.PositiveIntegerField(help_text="Bandwidth limit in GB")

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} subscribed to {self.plan.name}"
