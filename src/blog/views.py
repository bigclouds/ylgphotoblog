from django.shortcuts import render
from django.views.generic.detail import DetailView
from tagging.views import TaggedObjectList
from .models import Page, Photo


def index(request):
    photos = Photo.objects.all()
    featured_pages = Page.objects.filter(homepage_featured=True)
    template = 'blog/index.html'
    context = {'photos': photos, 'featured_pages': featured_pages}
    return render(request, template, context)


class TagView(TaggedObjectList):
    model = Photo


class PageView(DetailView):
    model = Page
