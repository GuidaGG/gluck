# Generated by Django 2.2.6 on 2019-11-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0005_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_title',
            field=models.TextField(default='section title', max_length=50),
        ),
    ]
