# Generated by Django 3.2.6 on 2021-11-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='post_code',
            field=models.CharField(default='post', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='state_county',
            field=models.CharField(default='post', max_length=80),
            preserve_default=False,
        ),
    ]