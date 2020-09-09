# Generated by Django 2.1 on 2018-12-15 06:11

import Main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20181201_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=Main.models.img_directory)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerdetails',
            name='image',
        ),
        migrations.AddField(
            model_name='attachment',
            name='customerdetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.CustomerDetails'),
        ),
    ]