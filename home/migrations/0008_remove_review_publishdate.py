# Generated by Django 4.0 on 2021-12-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='publishDate',
        ),
    ]