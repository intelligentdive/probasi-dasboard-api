# Generated by Django 4.0.1 on 2023-10-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oversea_recruitment', '0005_appointment_email_appointment_name_appointment_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservice',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
