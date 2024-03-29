# Generated by Django 2.1.1 on 2019-10-26 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gluck', '0006_auto_20191025_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Page')),
            ],
        ),
        migrations.AlterField(
            model_name='component',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gluck.Section'),
        ),
    ]
