# Generated by Django 2.0.1 on 2018-08-14 05:30

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
