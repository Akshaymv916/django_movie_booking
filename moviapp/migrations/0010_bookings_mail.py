# Generated by Django 5.0.7 on 2024-08-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviapp', '0009_alter_customeuser_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='mail',
            field=models.EmailField(default=True, max_length=254),
        ),
    ]
