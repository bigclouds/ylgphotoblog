from django.shortcuts import render
from django.views.generic.detail import DetailView
from tagging.views import TaggedObjectList
from .models import Page, Photo


def index(request):
    photos = Photo.objects.all()
    template = 'blog/index.html'
    context = {'photos': photos}
    return render(request, template, context)


class TagView(TaggedObjectList):
    model = Photo


class PageView(DetailView):
    model = Page
