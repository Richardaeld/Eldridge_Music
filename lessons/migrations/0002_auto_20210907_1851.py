# Generated by Django 3.2.6 on 2021-09-07 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_duration',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_start_time',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='new_lesson_day',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('lessons_per_week', models.DecimalField(decimal_places=0, max_digits=3)),
                ('duration_subscription_months', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('instrument_included', models.ManyToManyField(to='lessons.Instrument')),
                ('level_included', models.ManyToManyField(to='lessons.Instrument_Level')),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='instrument_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.instrument_level'),
        ),
    ]
