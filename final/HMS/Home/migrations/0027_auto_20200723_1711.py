# Generated by Django 3.0.8 on 2020-07-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0026_auto_20200723_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appeal',
            name='in_date',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='in_time',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='out_date',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='out_time',
        ),
        migrations.AddField(
            model_name='appeal',
            name='in_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appeal',
            name='out_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
