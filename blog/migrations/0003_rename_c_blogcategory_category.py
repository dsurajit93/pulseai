# Generated by Django 5.0.6 on 2024-06-20 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_category_blogcategory_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='c',
            new_name='category',
        ),
    ]
