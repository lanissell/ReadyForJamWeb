# Generated by Django 4.1.7 on 2023-03-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='BirthDate',
            field=models.DateField(auto_now=True),
        ),
    ]
