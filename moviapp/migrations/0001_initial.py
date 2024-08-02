# Generated by Django 5.0.7 on 2024-07-31 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('trailer', models.CharField(default='null', max_length=200)),
                ('date', models.CharField(default='null', max_length=20)),
                ('movi_desc', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('poster', models.ImageField(default='movi/poster/not.jpg', upload_to='movi/poster')),
                ('poster1', models.ImageField(default='movi/poster/not.jpg', upload_to='movi/poster')),
                ('genre', models.CharField(default='Action | Romance | comdey', max_length=50)),
                ('duration', models.CharField(max_length=10)),
                ('language', models.CharField(default='malayalam', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(default='movi/navbar/not.jpg', upload_to='movi/navbar')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(default='manager', max_length=30)),
                ('movi_name', models.CharField(max_length=100)),
                ('poster', models.ImageField(default='movi/navbar/not.jpg', upload_to='movi/navbar')),
                ('screen', models.CharField(default='null', max_length=10)),
                ('phoneno', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('shows', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_shows', to='moviapp.cinema')),
                ('date', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='moviapp.dates')),
                ('movi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movi_shows', to='moviapp.movie')),
                ('time', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='moviapp.time')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviapp.show')),
            ],
        ),
        migrations.CreateModel(
            name='Seatbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.BooleanField(default=False)),
                ('a2', models.BooleanField(default=False)),
                ('a3', models.BooleanField(default=False)),
                ('a4', models.BooleanField(default=False)),
                ('a5', models.BooleanField(default=False)),
                ('a6', models.BooleanField(default=False)),
                ('a7', models.BooleanField(default=False)),
                ('a8', models.BooleanField(default=False)),
                ('a9', models.BooleanField(default=False)),
                ('a10', models.BooleanField(default=False)),
                ('b1', models.BooleanField(default=False)),
                ('b2', models.BooleanField(default=False)),
                ('b3', models.BooleanField(default=False)),
                ('b4', models.BooleanField(default=False)),
                ('b5', models.BooleanField(default=False)),
                ('b6', models.BooleanField(default=False)),
                ('b7', models.BooleanField(default=False)),
                ('b8', models.BooleanField(default=False)),
                ('b9', models.BooleanField(default=False)),
                ('b10', models.BooleanField(default=False)),
                ('c1', models.BooleanField(default=False)),
                ('c2', models.BooleanField(default=False)),
                ('c3', models.BooleanField(default=False)),
                ('c4', models.BooleanField(default=False)),
                ('c5', models.BooleanField(default=False)),
                ('c6', models.BooleanField(default=False)),
                ('c7', models.BooleanField(default=False)),
                ('c8', models.BooleanField(default=False)),
                ('c9', models.BooleanField(default=False)),
                ('c10', models.BooleanField(default=False)),
                ('d1', models.BooleanField(default=False)),
                ('d2', models.BooleanField(default=False)),
                ('d3', models.BooleanField(default=False)),
                ('d4', models.BooleanField(default=False)),
                ('d5', models.BooleanField(default=False)),
                ('d6', models.BooleanField(default=False)),
                ('d7', models.BooleanField(default=False)),
                ('d8', models.BooleanField(default=False)),
                ('d9', models.BooleanField(default=False)),
                ('d10', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviapp.dates')),
                ('movi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviapp.movie')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviapp.time')),
            ],
        ),
    ]
