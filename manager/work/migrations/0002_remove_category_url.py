# Generated by Django 4.0.1 on 2022-03-02 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
