import datetime

from django.utils.deprecation import MiddlewareMixin
from analytics.utils import record_for_request


class AnalyticsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):

        record_for_request(datetime.date.today(), request.method, response.status_code)
        return response
