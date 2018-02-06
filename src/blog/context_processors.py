from django.conf import settings

from .models import Page


def config_processor(request):
    config = {
       'BLOG_NAME': settings.BLOG_NAME,
       'BLOG_DESCRIPTION': settings.BLOG_DESCRIPTION,
       'SEO_NOINDEX': settings.SEO_NOINDEX,
       'SOCIAL_PROFILES': settings.SOCIAL_PROFILES,
       'DEVIANTART_URL': settings.DEVIANTART_URL,
       'GOOGLEPLUS_URL': settings.GOOGLEPLUS_URL,
       'FACEBOOK_URL': settings.FACEBOOK_URL,
       'INSTAGRAM_URL': settings.INSTAGRAM_URL,
       'LINKEDIN_URL': settings.LINKEDIN_URL,
       'PINTEREST_URL': settings.PINTEREST_URL,
       'TUMBLR_URL': settings.TUMBLR_URL,
       'TWITTER_URL': settings.TWITTER_URL,

    }
    return {'config': config}


def nav_processor(request):
    return {'nav_items': Page.objects.filter(show_in_menu=True)}
