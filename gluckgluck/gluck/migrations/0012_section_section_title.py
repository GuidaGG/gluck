# Generated by Django 2.2.6 on 2019-11-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0011_remove_section_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_title',
            field=models.TextField(default='section title', max_length=50),
        ),
    ]
