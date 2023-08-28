# Generated by Django 4.0.7 on 2022-09-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_synthetic_rubber_give_vendor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='synthetic_rubber',
            name='check_remaining1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='synthetic_rubber',
            name='fixing_date1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='synthetic_rubber',
            name='send_fixing_date1',
            field=models.BooleanField(default=False),
        ),
    ]
