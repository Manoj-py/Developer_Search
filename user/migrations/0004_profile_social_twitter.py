# Generated by Django 4.0.1 on 2022-07-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_reated_profile_created_profile_location_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
