import datetime

from analytics.models import AnalyticsRequestsRecord


def add_analytics_record(request_type, response_status):

    requests_record, created = AnalyticsRequestsRecord.objects.get_or_create(
        date=datetime.date.today(),
    )

    if request_type == 'POST':
        requests_record.requests_counter_post += 1
        if response_status != 200:
            requests_record.requests_counter_post_err += 1

    else:
        requests_record.requests_counter_get += 1
        if response_status != 200:
            requests_record.requests_counter_get_err += 1
    requests_record.save()
