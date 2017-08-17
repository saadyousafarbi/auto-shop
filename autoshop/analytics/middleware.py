import datetime

from django.utils.deprecation import MiddlewareMixin
from analytics.utils import add_analytics_record


class AnalyticsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):

        add_analytics_record(request.method, response.status_code)
        return response
