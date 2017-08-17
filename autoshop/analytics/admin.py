from django.contrib import admin
from analytics.models import AnalyticsRequestsRecord


class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ['date']

admin.site.register(AnalyticsRequestsRecord, AnalyticsAdmin)
