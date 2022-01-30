# Generated by Django 3.2.11 on 2022-01-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(default=None, max_length=150, verbose_name='Short event description'),
        ),
    ]