# Generated by Django 4.0.7 on 2022-09-29 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0017_synthetic_rubber_check_remaining1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='natural_rubber',
            name='send_process_nal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='synthetic_rubber',
            name='send_process_syn',
            field=models.BooleanField(default=False),
        ),
    ]
