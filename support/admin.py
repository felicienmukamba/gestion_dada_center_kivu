from django.contrib import admin
from .models import SupportTicket

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at', 'updated_at', 'resolved')
    search_fields = ('user__username', 'subject', 'description')
    list_filter = ('resolved', 'created_at', 'updated_at')
    raw_id_fields = ('user',)
