from django.db import models
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField
from tagging.fields import TagField


class Photo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField('published date', blank=True)
    title = models.CharField(max_length=200)
    image = ThumbnailerImageField()
    description = models.TextField(blank=True, null=True)
    tags = TagField()

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)
