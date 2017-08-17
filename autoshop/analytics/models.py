import datetime

from django.db import models


class AnalyticsRequestsRecord(models.Model):
    """
    AnalyticsRequestsRecord to record all the request for the site.

    Fields:
         date (date) = date of request
         request_counter_get (int) = success counter for GET request
         request_counter_get_err (int) = failure counter for GET request
         requests_counter_post (int) = success counter for POST request
         requests_counter_post_err (int) = failure counter for POST request

    """
    date = models.DateField(verbose_name='Record Date', default=datetime.date.today, unique=True)
    requests_counter_get = models.PositiveIntegerField(verbose_name='GET Requests Counter', default=0)
    requests_counter_get_err = models.PositiveIntegerField(verbose_name='Failed GET Requests Counter', default=0)
    requests_counter_post = models.PositiveIntegerField(verbose_name='POST Requests Counter', default=0)
    requests_counter_post_err = models.PositiveIntegerField(verbose_name='Failed POST Requests Counter', default=0)
