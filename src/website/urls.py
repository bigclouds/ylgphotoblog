from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('%s/' % settings.CONTACT_PAGE_SLUG, include('contact_form.urls')),
    path('blog/', include('blog.urls')),
    path('videos/', include('videos.urls')),
    path(r'', views.HomeView),
]


# Serving media files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT1, show_indexes=True)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.HTML_URL, document_root=settings.HTML_ROOT, show_indexes=False)
