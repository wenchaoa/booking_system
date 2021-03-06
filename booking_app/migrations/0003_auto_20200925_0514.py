# Generated by Django 2.1.5 on 2020-09-25 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_auto_20200918_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datelabel', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Timeperiod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timelabel', models.CharField(max_length=128)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.Date')),
            ],
        ),
        migrations.RenameField(
            model_name='building',
            old_name='bname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='rname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='building',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='building',
            name='views',
        ),
        migrations.RemoveField(
            model_name='room',
            name='url',
        ),
        migrations.AddField(
            model_name='room',
            name='bookmarked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='manager',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='timeperiod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.Timeperiod'),
        ),
        migrations.AddField(
            model_name='date',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.Room'),
        ),
    ]
