from django.conf import settings

from .models import Page


def config_processor(request):
    config = {
       'BLOG_NAME': settings.BLOG_NAME,
       'BLOG_DESCRIPTION': settings.BLOG_DESCRIPTION,
       'SEO_NOINDEX': settings.SEO_NOINDEX,
    }
    return {'config': config}


def nav_processor(request):
    return {'nav_items': Page.objects.filter(show_in_menu=True)}
