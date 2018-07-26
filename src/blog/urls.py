from django.urls import path

from .views import HomepageView, PageView, TagView, tag_list

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('tags/', tag_list, name='tag-list'),
    path('tag/<str:tag>/', TagView.as_view(), name='tag-view'),
    path('<slug:slug>/', PageView.as_view(), name='page-view'),
]
