# Generated by Django 2.2.6 on 2019-11-06 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0013_text_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='image',
            new_name='imaget',
        ),
    ]
