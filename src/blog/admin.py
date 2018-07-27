from django.contrib import admin
from .models import Page, Photo

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
        #print(request.user.id)
        #print(queryset.filter(author_id=2))
        self.lookup_choices = ()
        if not request.user.is_superuser:
            return queryset.filter(author_id=request.user.id)
        else:
            return queryset.filter()

class PageAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PhotoAdmin(admin.ModelAdmin):
    list_filter = (AuthDecadeBornListFilter,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

admin.site.register(Page, PageAdmin)
admin.site.register(Photo, PhotoAdmin)
