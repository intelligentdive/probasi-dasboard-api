# Generated by Django 4.0.1 on 2023-10-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicename', '0002_rename_task_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='completed',
        ),
    ]