# Generated by Django 2.2.6 on 2019-11-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0009_auto_20191104_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='section_fk',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='section_fk',
            new_name='section',
        ),
    ]