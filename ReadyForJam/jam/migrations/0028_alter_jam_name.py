# Generated by Django 4.2.1 on 2023-05-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0027_remove_projectcolor_project_delete_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jam',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
