from django.conf import settings
from django.contrib.sites.models import Site


def site_processor(request):
    """
    Provide site object and common project settings across all project in context.
    """
    return {
        'settings': settings,
        'site': Site.objects.get_current(),
    }
