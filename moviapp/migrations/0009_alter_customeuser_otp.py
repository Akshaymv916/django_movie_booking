# Generated by Django 5.0.7 on 2024-07-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviapp', '0008_customeuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]
