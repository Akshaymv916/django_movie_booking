# Generated by Django 5.0.7 on 2024-07-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviapp', '0006_alter_bookings_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatbook',
            name='seatcount',
            field=models.IntegerField(default=0),
        ),
    ]