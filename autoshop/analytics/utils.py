from django.db.models import F

from analytics.models import AnalyticsRequestsRecord


def record_for_request(date, request_type, response_status):

    record = AnalyticsRequestsRecord.objects.update_or_create(
        date=date,
    )
    if 'GET' in request_type:
        if response_status == 200:
            record.count = F('request_counter_get') + 1
            record.save()
            return None
        record.count = F('request_counter_get_err') + 1
        record.save()
        return None

    elif 'POST' in request_type:
        if response_status == 200:
            record.count = F('request_counter_post') + 1
            record.save()
            return None
        record.count = F('request_counter_post_err') + 1
        record.save()
        return None
