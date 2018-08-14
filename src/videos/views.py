from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from tagging.models import Tag
from tagging.utils import LOGARITHMIC
from tagging.views import TaggedObjectList

from .models import Video

def generate_tag_cloud(filters=None, nolimit=False):
    cloud = Tag.objects.cloud_for_model(
        Video,
        steps=9,
        distribution=LOGARITHMIC,
        filters=filters,
        min_count=None)
    if not nolimit:
        limit = settings.TAG_CLOUD_LIMIT
        if len(cloud) > limit:
            while len(cloud) > limit:
                min_value = min(tag.count for tag in cloud)
                min_tag = [tag for tag in cloud if tag.count == min_value][0]
                cloud.remove(min_tag)
    return cloud


def generate_related_tags(tag):
    tags = Tag.objects.related_for_model(
        tag,
        Video,
        counts=True,
        min_count=None)
    limit = settings.RELATED_TAGS_LIMIT
    if len(tags) > limit:
        while len(tags) > limit:
            min_value = min(tag.count for tag in tags)
            min_tag = [tag for tag in tags if tag.count == min_value][0]
            tags.remove(min_tag)
    return tags

#class HomeVideoView(View):
class HomeVideoView(ListView):
    model = Video
    context_object_name = 'videos'
    paginate_by = 10
    template_name = "videos/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        d = super().dispatch(*args, **kwargs)
        context = self.get_context_data(**kwargs)
        #context['view'] = 'homevideo-view'
        #context['page_title'] = "Video SHow" #settings.BLOG_NAME
        #context['page_description'] = "Video Desc"  #settings.BLOG_DESCRIPTION
        return render(self.request, "videos/index.html", context=context)
        #return render(self.request, "videos/index.html")

    def get_queryset(self):
        u = self.request.user
        filters = dict()
        if not u.is_superuser:
            filters = dict(author_id=u.id)
        return QuerySet(model=Video).filter(**filters)

    def get_context_data(self, **kwargs):
        u = self.request.user
        filters = None
        context = super().get_context_data(**kwargs)
        context['view'] = 'homevideo-view'
        context['page_title'] = "Video SHow" #settings.BLOG_NAME
        context['page_description'] = "Video Desc"  #settings.BLOG_DESCRIPTION

        if u.is_superuser:
            context['all_videos'] = Video.objects.all()
        else:
            context['all_videos'] = Video.objects.filter(author_id=u.id)
            filters = dict(author_id=u.id)
        #context['tag_cloud'] = generate_tag_cloud(filters=filters)
        return context


class TagView(TaggedObjectList):
    model = Video
    context_object_name = 'videos'
    paginate_by = 10
    allow_empty = True

    #def get_queryset(self):
        #u = self.request.user
        #filters = None
        #if not u.is_superuser:
        #    filters = dict(author_id=u.id)
        #self.tag_instance = QuerySet(model=Tag).filter(name=self.tag)
        #return QuerySet(model=Tag).filter(name=self.tag)
        #return QuerySet(model=Video).filter(**filters)

    def get_context_data(self, **kwargs):
        u = self.request.user
        filters = dict(tags__icontains=self.tag)
        context = super().get_context_data(**kwargs)
        context['view'] = 'tag-view'
        context['page_title'] = '#{} videos'.format(self.tag)
        if u.is_superuser:
            context['all_videos'] = Video.objects.filter(**filters)
        else:
            filters.update(dict(author_id=u.id))
            context['all_videos'] = Video.objects.filter(**filters)
        context['tag_cloud'] = generate_tag_cloud(filters=filters)
        context['page_description'] = 'Videos tagged with #{}'.format(self.tag)
        context['related_tags'] = generate_related_tags(self.tag)
        return context

def tag_list(request):
    u = request.user
    filters = None
    if not u.is_superuser:
        filters = dict(author_id=u.id)

    tag_cloud = generate_tag_cloud(nolimit=True, filters=filters)
    template = 'videos/tag_list.html'
    context = {
        'page_title': 'Tags',
        'tag_cloud': tag_cloud}
    return render(request, template, context)
