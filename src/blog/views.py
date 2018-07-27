from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.query import QuerySet

from tagging.models import Tag
from tagging.utils import LOGARITHMIC
from tagging.views import TaggedObjectList

from .models import Page, Photo


def generate_tag_cloud(filters=None, nolimit=False):
    cloud = Tag.objects.cloud_for_model(
        Photo,
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
        Photo,
        counts=True,
        min_count=None)
    limit = settings.RELATED_TAGS_LIMIT
    if len(tags) > limit:
        while len(tags) > limit:
            min_value = min(tag.count for tag in tags)
            min_tag = [tag for tag in tags if tag.count == min_value][0]
            tags.remove(min_tag)
    return tags

class HomepageView(ListView):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 5

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        u = self.request.user
        s = QuerySet(model=Photo).filter(author_id=u.id)
        return QuerySet(model=Photo).filter(author_id=u.id)

    def get_context_data(self, **kwargs):
        u = self.request.user
        context = super().get_context_data(**kwargs)
        context['view'] = 'homepage-view'
        if settings.SEO_BLOG_TITLE:
            context['page_title'] = settings.SEO_BLOG_TITLE
        else:
            context['page_title'] = settings.BLOG_NAME
        if settings.SEO_BLOG_DESCRIPTION:
            context['page_description'] = settings.SEO_BLOG_DESCRIPTION
        elif settings.BLOG_DESCRIPTION:
            context['page_description'] = settings.BLOG_DESCRIPTION
        context['featured_pages'] = Page.objects.filter(homepage_featured=True)
        if u.is_superuser:
            context['all_photos'] = Photo.objects.all()
        else:
            context['all_photos'] = Photo.objects.filter(author_id=u.id)
        filters = dict(author_id=u.id)
        context['tag_cloud'] = generate_tag_cloud(filters=filters)
        return context


class TagView(TaggedObjectList):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        u = self.request.user
        context = super().get_context_data(**kwargs)
        context['view'] = 'tag-view'
        context['page_title'] = '#{} photos'.format(self.tag)
        if u.is_superuser:
            context['all_photos'] = Photo.objects.all()
        else:
            context['all_photos'] = Photo.objects.filter(author_id=u.id)
        context['page_description'] = 'Photos tagged with #{}'.format(self.tag)
        filters = dict(author_id=u.id)
        context['tag_cloud'] = generate_tag_cloud(filters=filters)
        context['related_tags'] = generate_related_tags(self.tag)
        return context


class PageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'page-view'
        page = self.object
        if page.seo_title:
            context['page_title'] = page.seo_title
        else:
            context['page_title'] = page.title
        if page.seo_description:
            context['page_description'] = page.seo_description
        if page.page_head:
            context['page_head'] = page.page_head
        if page.page_styles:
            context['page_styles'] = page.page_styles
        return context


def tag_list(request):
    u = request.user
    filters = dict(author_id=u.id)
    tag_cloud = generate_tag_cloud(nolimit=True, filters=filters)
    template = 'blog/tag_list.html'
    context = {
        'page_title': 'Tags',
        'tag_cloud': tag_cloud}
    return render(request, template, context)
