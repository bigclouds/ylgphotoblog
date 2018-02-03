from .models import Page


# Makes nav_items variable available for all templates
def nav_processor(request):
    return {'nav_items': Page.objects.filter(show_in_menu=True)}
