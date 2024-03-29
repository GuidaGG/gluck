# Generated by Django 2.2.6 on 2019-11-04 14:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='new page', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField(default='title', max_length=200)),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Section')),
            ],
        ),
    ]
