# Generated by Django 3.0.8 on 2020-07-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_auto_20200723_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='in_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appeal',
            name='reason',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
