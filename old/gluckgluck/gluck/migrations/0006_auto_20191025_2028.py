# Generated by Django 2.2.6 on 2019-10-25 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0005_auto_20191025_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Page'),
        ),
    ]
