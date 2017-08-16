import datetime
from analytics.models import AnalyticsRequestsRecord


class AnalyticsMiddleware:

    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        response = self.response(request)
        request_type = request.method
        request_date = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:
            response_status = 'Success'
        elif response_status == 404:
            response_status = 'Failure'
        # AnalyticsRequestsRecord.objects.create(
        #     date=request_date,
        #     request_type=request_type,
        #     request_status=response_status,
        # )
        return response
