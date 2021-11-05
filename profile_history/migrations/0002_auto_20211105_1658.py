# Generated by Django 3.2.6 on 2021-11-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile_history',
            old_name='default_street_address',
            new_name='default_street_address_billing',
        ),
        migrations.RemoveField(
            model_name='user_profile_history',
            name='default_prefered_name',
        ),
        migrations.RemoveField(
            model_name='user_profile_history',
            name='default_pronouns',
        ),
        migrations.AddField(
            model_name='user_profile_history',
            name='default_street_address_shipping',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
