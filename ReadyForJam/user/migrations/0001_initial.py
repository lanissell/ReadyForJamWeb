# Generated by Django 4.1.7 on 2023-03-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NickName', models.CharField(max_length=255)),
                ('Rate', models.IntegerField(default=0)),
                ('IsLeader', models.BooleanField(default=False)),
                ('TeamId', models.IntegerField(default=0)),
                ('AvatarUrl', models.ImageField(upload_to='')),
            ],
        ),
    ]
