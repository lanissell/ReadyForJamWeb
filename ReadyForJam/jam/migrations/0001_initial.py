# Generated by Django 4.2.1 on 2023-05-19 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('theme', models.CharField(max_length=128)),
                ('avatar', models.ImageField(upload_to='jam/avatar')),
                ('content', django_ckeditor_5.fields.CKEditor5Field()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_team', models.BooleanField(default=True)),
                ('jam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jam.jam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JamDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=30)),
                ('voting_start_date', models.CharField(max_length=30)),
                ('voting_end_date', models.CharField(max_length=30)),
                ('time_zone', models.CharField(default='Asia/Krasnoyarsk', max_length=30)),
                ('jam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jam.jam')),
            ],
        ),
        migrations.CreateModel(
            name='JamCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('jam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jam.jam')),
            ],
        ),
        migrations.CreateModel(
            name='JamColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(max_length=10)),
                ('form_color', models.CharField(max_length=10)),
                ('main_text_color', models.CharField(max_length=10)),
                ('jam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jam.jam')),
            ],
        ),
    ]
