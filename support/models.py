from django.db import models
from django.contrib.auth import get_user_model

class SupportTicket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
