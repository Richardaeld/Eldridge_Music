# Generated by Django 3.2.6 on 2021-11-06 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_history', '0002_auto_20211105_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile_history',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='user_profile_history',
            name='default_full_name',
        ),
    ]