# Generated by Django 2.2.6 on 2019-11-04 15:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='new page', max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='published_date',
        ),
        migrations.AddField(
            model_name='event',
            name='subtitle',
            field=models.CharField(default='true', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Page')),
            ],
            options={
                'verbose_name': 'Component',
            },
        ),
    ]
