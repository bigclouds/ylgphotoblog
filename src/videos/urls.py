from django.urls import path

from .views import HomeVideoView, TagView, tag_list

urlpatterns = [
    path('', HomeVideoView.as_view(), name='homevideo-view'),
#    path('tags/', tag_list, name='videotag-list'),
#    path('tag/<str:tag>/', TagView.as_view(), name='videotag-view'),
]
