# Generated by Django 4.0 on 2022-01-01 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_news_ofgame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game')),
            ],
        ),
    ]
