from django.conf import settings
from .models import Page


def config_processor(request):
    config = {
       'BLOG_NAME': settings.BLOG_NAME,
    }
    return {'config': config}


# Makes nav_items variable available for all templates
def nav_processor(request):
    return {'nav_items': Page.objects.filter(show_in_menu=True)}
