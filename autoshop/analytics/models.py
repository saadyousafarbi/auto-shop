from __future__ import unicode_literals

from django.db import models


class AnalyticsRequestsRecord(models.Model):
    """
    AnalyticsRequestsRecord to record all the request for the site.

    Fields:
        date (date) = date of request
        request_status (bool) = success/error property of request
        request_type (str) = type of request
    """
    REQUEST_CHOICES = (
        ('G', 'GET'),
        ('P', 'POST'),
    )

    date = models.DateField()
    request_status = models.BooleanField()
    request_type = models.CharField(choices=REQUEST_CHOICES)
