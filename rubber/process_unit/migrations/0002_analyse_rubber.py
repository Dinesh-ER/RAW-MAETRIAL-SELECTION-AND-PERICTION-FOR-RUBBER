# Generated by Django 4.0.7 on 2022-10-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='analyse_rubber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=200)),
                ('recycle', models.CharField(max_length=200)),
                ('compound', models.CharField(max_length=200)),
                ('chemical_formula', models.CharField(max_length=200)),
                ('polymer', models.CharField(max_length=200)),
                ('mixing', models.CharField(max_length=200)),
                ('made_from_type', models.CharField(max_length=200)),
            ],
        ),
    ]