# Generated by Django 5.0.7 on 2024-07-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviapp', '0004_alter_bookings_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='time',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
    ]