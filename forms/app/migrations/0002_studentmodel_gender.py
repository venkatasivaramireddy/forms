# Generated by Django 2.2.5 on 2019-11-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
