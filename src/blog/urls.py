from django.urls import path, re_path

from tagging.views import TaggedObjectList

from .models import Photo
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.PageView.as_view(), name='page-view'),
    re_path(r'^tag/(?P<tag>[^/]+(?u))/$', TaggedObjectList.as_view(
            model=Photo,
            paginate_by=10,
            allow_empty=True,
            related_tags=True), name='tag-view'
            ),
]
