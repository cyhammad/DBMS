# Generated by Django 4.0 on 2021-12-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_rating_game_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameImage',
            field=models.ImageField(default='something', upload_to=''),
        ),
    ]
