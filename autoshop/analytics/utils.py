from django.db.models import F

from analytics.models import AnalyticsRequestsRecord


def record_for_request(date, request_type, response_status):

    record, created = AnalyticsRequestsRecord.objects.get_or_create(
        date=date,
    )
    if 'GET' in request_type:
        if response_status == 200:
            record.requests_counter_get = F('requests_counter_get') + 1
            record.save()
            return None
        record.requests_counter_get_err = F('requests_counter_get_err') + 1
        record.save()
        return None

    elif 'POST' in request_type:
        if response_status == 200:
            record.requests_counter_post = F('requests_counter_post') + 1
            record.save()
            return None
        record.requests_counter_post_err = F('requests_counter_post_err') + 1
        record.save()
        return None
