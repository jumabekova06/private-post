# Generated by Django 2.2.24 on 2022-06-01 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='public',
            new_name='private',
        ),
    ]
