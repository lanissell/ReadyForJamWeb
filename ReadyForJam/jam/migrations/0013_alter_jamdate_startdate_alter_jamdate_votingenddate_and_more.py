# Generated by Django 4.1.7 on 2023-04-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0012_alter_participant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamdate',
            name='startDate',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jamdate',
            name='votingEndDate',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jamdate',
            name='votingStartDate',
            field=models.CharField(max_length=30),
        ),
    ]