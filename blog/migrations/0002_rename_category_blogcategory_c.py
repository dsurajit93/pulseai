# Generated by Django 5.0.6 on 2024-06-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='category',
            new_name='c',
        ),
    ]
