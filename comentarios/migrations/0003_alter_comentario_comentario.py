# Generated by Django 4.1.3 on 2022-11-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comentario_email_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(default=True),
        ),
    ]
