# Generated by Django 2.1 on 2018-08-24 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feature',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
