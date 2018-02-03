from django.shortcuts import render

from tagging.views import TaggedObjectList

from .models import Photo


def index(request):
    photos = Photo.objects.all()
    template = 'blog/index.html'
    context = {'photos': photos}
    return render(request, template, context)


class TagView(TaggedObjectList):
    model = Photo
