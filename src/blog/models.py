from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField
from tagging.fields import TagField


class Photo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField('published date', blank=True)
    title = models.CharField(max_length=200)
    image = ThumbnailerImageField()
    #description = models.TextField(blank=True, null=True)
    description = RichTextField()
    tags = TagField()

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        if not self.tags:
            self.tags = self.date.strftime("%Y-%m-%d")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextUploadingField(blank=True, null=True)
    show_in_menu = models.BooleanField(default=True)
    menu_position = models.IntegerField(default=0)
    homepage_featured = models.BooleanField(default=False)
    featured_image = ThumbnailerImageField(blank=True, null=True)
    seo_title = models.CharField(max_length=200, blank=True, null=True)
    seo_description = models.CharField(max_length=200, blank=True, null=True)
    seo_noindex = models.BooleanField(default=False)
    page_head = models.TextField(blank=True, null=True)
    page_styles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('menu_position',)
