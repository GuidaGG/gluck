# Generated by Django 2.2.6 on 2019-11-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0012_section_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]