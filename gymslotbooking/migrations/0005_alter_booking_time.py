# Generated by Django 4.2.11 on 2024-04-23 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymslotbooking', '0004_alter_booking_date_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 23, 8, 38, 18, 350750)),
        ),
    ]
