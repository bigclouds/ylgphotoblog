from django.conf import settings
from django.db import models
from django.utils import timezone
from tagging.fields import TagField
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField
from videokit.models import VideoSpecField
from videokit.models import VideoField

# Create your models here.

class Video(models.Model):
    video = VideoField(upload_to = "video/", null = True, blank = True,
	width_field = 'video_width', height_field = 'video_height',
	rotation_field = 'video_rotation',
	mimetype_field = 'video_mimetype',
	duration_field = 'video_duration',
	thumbnail_field = 'video_thumbnail')
    description = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="")
    date = models.DateTimeField('published date', blank=True)
    video_width = models.IntegerField(null = True, blank = True)
    video_height = models.IntegerField(null = True, blank = True)
    video_rotation = models.FloatField(null = True, blank = True)
    video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
    video_duration = models.IntegerField(null = True, blank = True, editable=True)
    video_thumbnail = models.ImageField(null = True, blank = True)
    shared = models.BooleanField(default=True)
    tags = TagField()
    #video_mp4 = VideoSpecField(source = 'video', format = 'mp4')
    #video_ogg = VideoSpecField(source = 'video', format = 'ogg')
    #video_webm = VideoSpecField(source = 'video', format = 'webm')
    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        if not self.tags:
            self.tags = self.date.strftime(settings.TAGS_FORMAT)
        super().save(*args, **kwargs)

        def __str__(self):
            return self.title

        class Meta:
            ordering = ('-date',)
