# Generated by Django 3.0.8 on 2020-07-22 17:42

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_staff_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(default='default.png', null=True, upload_to='', validators=[Home.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='default.png', null=True, upload_to='', validators=[Home.models.validate_image]),
        ),
    ]
