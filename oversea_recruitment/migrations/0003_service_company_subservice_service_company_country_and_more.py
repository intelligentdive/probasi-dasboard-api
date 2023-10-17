# Generated by Django 4.0.1 on 2023-10-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oversea_recruitment', '0002_subservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_company',
            name='Subservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oversea_recruitment.subservice'),
        ),
        migrations.AddField(
            model_name='service_company',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service_company',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
