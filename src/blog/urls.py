from django.urls import path

from .views import HomepageView, PageView, TagView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('<slug:slug>/', PageView.as_view(), name='page-view'),
    path('tag/<str:tag>/', TagView.as_view(), name='tag-view'),
]
