# Generated by Django 4.2.1 on 2023-05-13 08:37

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0028_alter_jam_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jam',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
    ]
