# Generated by Django 3.2.9 on 2021-11-25 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211125_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 25, 19, 54, 36, 153404, tzinfo=utc)),
        ),
    ]