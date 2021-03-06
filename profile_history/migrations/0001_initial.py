# Generated by Django 3.2.6 on 2021-11-17 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('default_street_address_1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address_2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_state_county', models.CharField(blank=True, max_length=80, null=True)),
                ('default_post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
