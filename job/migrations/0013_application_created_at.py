# Generated by Django 3.1.5 on 2021-01-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_application_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
