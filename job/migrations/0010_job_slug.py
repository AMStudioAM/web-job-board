# Generated by Django 3.1.5 on 2021-01-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_remove_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
