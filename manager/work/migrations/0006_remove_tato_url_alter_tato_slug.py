# Generated by Django 4.0.1 on 2022-03-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_tato_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tato',
            name='url',
        ),
        migrations.AlterField(
            model_name='tato',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
    ]
