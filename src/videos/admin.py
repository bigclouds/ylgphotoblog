from django.contrib import admin
from .models import Video

class AuthDecadeBornListFilter(admin.SimpleListFilter):
    title = 'filter user id'
    parameter_name = 'decade'
    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            a = model_admin.model.objects.all()
            return a
        else:
            a = model_admin.model.objects.filter(author_id=request.user.id)
            return a
    def queryset(self, request, queryset):
        self.lookup_choices = ()
        if not request.user.is_superuser:
            return queryset.filter(author_id=request.user.id)
        else:
            return queryset.filter()

class VideoAdmin(admin.ModelAdmin):
    exclude = ('date','author',)
    list_filter = (AuthDecadeBornListFilter,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

admin.site.register(Video, VideoAdmin)
