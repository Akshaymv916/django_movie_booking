# Generated by Django 5.0.7 on 2024-07-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviapp', '0003_delete_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
