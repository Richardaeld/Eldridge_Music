# Generated by Django 3.2.6 on 2021-09-27 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_remove_instrument_friendly_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('image_url', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='duration_subscription_months',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
        migrations.AddField(
            model_name='subscription',
            name='active_subscription',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='lesson_class_type',
            field=models.CharField(choices=[('private', 'private'), ('group', 'group'), ('prerecorded', 'prerecorded')], default='prerecorded', max_length=11),
        ),
        migrations.AddField(
            model_name='subscription',
            name='lesson_time_length',
            field=models.DecimalField(blank=True, choices=[('0.50', '0.50'), ('0.75', '0.75'), ('1.00', '1.00')], decimal_places=0, default='1.00', max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_duration_months',
            field=models.DecimalField(choices=[('.97', '.97'), ('.94', '.94'), ('.91', '.91'), ('.88', '.88')], decimal_places=0, default='.88', max_digits=2),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='lessons_per_week',
            field=models.DecimalField(choices=[('1', '1'), ('2', '2'), ('3', '3')], decimal_places=1, default='1', max_digits=1),
        ),
        migrations.AddField(
            model_name='subscription',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.image'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.image'),
        ),
    ]