
from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'status', 'priority')  # Fields to display in the list view
    list_filter = ('status', 'priority')  # Filters for the admin list view
    list_editable = ('status',)  # Allow editing of status directly in the list view

admin.site.register(Complaint, ComplaintAdmin)