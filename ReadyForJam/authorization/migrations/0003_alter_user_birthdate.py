# Generated by Django 4.1.7 on 2023-03-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='BirthDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]