# Generated by Django 4.0.7 on 2022-09-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_natural_rubber_send_fixing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='natural_rubber',
            name='natural_id',
            field=models.IntegerField(null=True),
        ),
    ]
