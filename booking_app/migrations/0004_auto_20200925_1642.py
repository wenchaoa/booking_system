# Generated by Django 2.1.5 on 2020-09-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_auto_20200925_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
