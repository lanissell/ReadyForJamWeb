# Generated by Django 4.1.7 on 2023-03-26 07:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0004_jam_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='jam',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='none'),
        ),
    ]