# Generated by Django 4.1.7 on 2023-03-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0009_jamcolor_jam_jamcriteria_jam_jamdate_jam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jam',
            name='avatar',
            field=models.ImageField(upload_to='jam/avatar'),
        ),
    ]