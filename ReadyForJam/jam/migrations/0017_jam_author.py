# Generated by Django 4.1.7 on 2023-04-20 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jam', '0016_alter_jamdate_startdate_alter_jamdate_votingenddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jam',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]