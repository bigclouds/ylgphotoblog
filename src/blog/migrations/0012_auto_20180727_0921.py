# Generated by Django 2.0.1 on 2018-07-27 07:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180204_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
