# Generated by Django 4.2.11 on 2024-05-09 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Concerts',
            new_name='Concert',
        ),
    ]
