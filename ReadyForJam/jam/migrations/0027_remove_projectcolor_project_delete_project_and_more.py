# Generated by Django 4.2.1 on 2023-05-11 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0026_rename_description_project_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcolor',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectColor',
        ),
    ]
