# Generated by Django 4.0 on 2022-01-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_category_options_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prizePool', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]