from django.conf import settings
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from tagging.views import TaggedObjectList

from .models import Page, Photo


class HomepageView(ListView):
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'homepage-view'
        context['page_title'] = settings.BLOG_NAME
        context['featured_pages'] = Page.objects.filter(homepage_featured=True)
        if settings.BLOG_DESCRIPTION:
            context['page_description'] = settings.BLOG_DESCRIPTION
        return context


class TagView(TaggedObjectList):
    model = Photo
    context_object_name = 'photos'
    allow_empty = True
    related_tags = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'tag-view'
        context['page_title'] = '#{} photos - {}'.format(self.tag,
                                                         settings.BLOG_NAME)
        context['page_description'] = 'Photos tagged with #{}.'.format(self.tag)
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
        if page.page_styles:
            context['page_styles'] = page.page_styles
        if page.page_scripts:
            context['page_scripts'] = page.page_scripts
        return context
