# Generated by Django 4.0 on 2022-01-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_update_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categorie'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='fooCat', max_length=300),
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.CharField(default='fooGenre', max_length=300),
        ),
    ]
