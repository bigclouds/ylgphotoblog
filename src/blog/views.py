from django.conf import settings
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tagging.models import Tag
from tagging.utils import LOGARITHMIC
from tagging.views import TaggedObjectList

from .models import Page, Photo


def generate_tag_cloud():
    cloud = Tag.objects.cloud_for_model(
        Photo,
        steps=9,
        distribution=LOGARITHMIC,
        filters=None,
        min_count=None)
    limit = settings.TAG_CLOUD_LIMIT
    if len(cloud) > limit:
        while len(cloud) > limit:
            min_value = min(tag.count for tag in cloud)
            min_tag = [tag for tag in cloud if tag.count == min_value][0]
            # print('removing {} - {} counts'.format(min_tag, min_tag.count))
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
            # print('removing {} - {} counts'.format(min_tag, min_tag.count))
            tags.remove(min_tag)
    return tags


class HomepageView(ListView):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'homepage-view'
        context['page_title'] = settings.BLOG_NAME
        context['featured_pages'] = Page.objects.filter(homepage_featured=True)
        context['all_photos'] = Photo.objects.all()
        if settings.BLOG_DESCRIPTION:
            context['page_description'] = settings.BLOG_DESCRIPTION
        context['tag_cloud'] = generate_tag_cloud()
        return context


class TagView(TaggedObjectList):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'tag-view'
        context['page_title'] = '#{} photos - {}'.format(self.tag,
                                                         settings.BLOG_NAME)
        context['all_photos'] = Photo.objects.all()
        context['page_description'] = 'Photos tagged with #{}'.format(self.tag)
        context['tag_cloud'] = generate_tag_cloud()
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
            context['page_title'] = '{} - {}'.format(page.title,
                                                     settings.BLOG_NAME)
        if page.seo_description:
            context['page_description'] = page.seo_description
        if page.page_head:
            context['page_head'] = page.page_head
        if page.page_styles:
            context['page_styles'] = page.page_styles
        return context
