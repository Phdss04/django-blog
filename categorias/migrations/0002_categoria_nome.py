# Generated by Django 4.1.3 on 2022-11-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='nome',
            field=models.CharField(default=None, max_length=70),
        ),
    ]
