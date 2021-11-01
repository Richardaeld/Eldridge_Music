# Generated by Django 3.2.6 on 2021-10-28 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Music Styles',
            },
        ),
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('name', models.CharField(max_length=254)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('active_product', models.BooleanField(default=True)),
                ('stocked', models.BooleanField(default=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.CharField(blank=True, max_length=1024, null=True)),
                ('special', models.BooleanField(default=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchandise.music_style')),
            ],
            options={
                'verbose_name_plural': 'Merchandise',
            },
        ),
    ]