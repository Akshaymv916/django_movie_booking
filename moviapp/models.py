from datetime import datetime
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Navbar(models.Model):
    poster=models.ImageField(upload_to='movi/navbar',default="movi/navbar/not.jpg")


class Dates(models.Model):
    date = models.DateField()
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    
    
class Time(models.Model):
    time=models.TextField(max_length=50)
    def __str__(self):
        return str(self.time)

class Cinema(models.Model):
    cinema = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, default='manager')
    movi_name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movi/navbar', default="movi/navbar/not.jpg")
    screen = models.CharField(max_length=10, default="null")
    phoneno = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movi_name


class Movie(models.Model):
    movie=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    trailer=models.CharField(max_length=200,default="null")
    date=models.CharField(max_length=20,default="null")
    movi_desc=models.TextField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    poster=models.ImageField(upload_to='movi/poster',default="movi/poster/not.jpg")
    poster1=models.ImageField(upload_to='movi/poster',default="movi/poster/not.jpg")
    genre=models.CharField(max_length=50,default="Action | Romance | comdey")
    duration=models.CharField(max_length=10)
    language=models.CharField(default="malayalam",max_length=100)

    def __str__(self):
        return self.name

class Show(models.Model):
    shows=models.AutoField(primary_key=True)
    cinema=models.ForeignKey('Cinema',on_delete=models.CASCADE,related_name="cinema_shows")
    movi=models.ForeignKey('Movie',on_delete=models.CASCADE,related_name="movi_shows")
    time=models.ForeignKey(Time,on_delete=models.CASCADE,default=True)
    date=models.ForeignKey(Dates,on_delete=models.CASCADE,default=True)
    price=models.IntegerField()

    def __str__(self):
        return  self.movi.name +" | "+self.time.time +" | "+self.date.date.strftime('%Y-%m-%d')

class Bookings(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shows=models.ForeignKey(Show,on_delete=models.CASCADE)
    seat=models.CharField(max_length=100)
    time=models.ForeignKey(Time,on_delete=models.CASCADE,default=True,null=True)
    price=models.IntegerField(default=True)
    paymentid=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False)
    mail=models.EmailField(default=True)
    booking_date = models.DateField(auto_now_add=True)

    @property
    def seat_as__list(self):
        return self.seat.split('')
    def __str__(self):
        return self.user.username +" | "+ self.shows.cinema.movi_name +" | "+ self.seat
    
class Seatbook(models.Model):
    movi=models.ForeignKey(Movie,on_delete=models.CASCADE)
    date=models.ForeignKey(Dates,on_delete=models.CASCADE)
    time=models.ForeignKey(Time,on_delete=models.CASCADE)
    seatcount=models.IntegerField(default=0)
    a1=models.BooleanField(default=False)
    a2=models.BooleanField(default=False)
    a3=models.BooleanField(default=False)
    a4=models.BooleanField(default=False)
    a5=models.BooleanField(default=False)
    a6=models.BooleanField(default=False)
    a7=models.BooleanField(default=False)
    a8=models.BooleanField(default=False)
    a9=models.BooleanField(default=False)
    a10=models.BooleanField(default=False)

    b1=models.BooleanField(default=False)
    b2=models.BooleanField(default=False)
    b3=models.BooleanField(default=False)
    b4=models.BooleanField(default=False)
    b5=models.BooleanField(default=False)
    b6=models.BooleanField(default=False)
    b7=models.BooleanField(default=False)
    b8=models.BooleanField(default=False)
    b9=models.BooleanField(default=False)
    b10=models.BooleanField(default=False)

    c1=models.BooleanField(default=False)
    c2=models.BooleanField(default=False)
    c3=models.BooleanField(default=False)
    c4=models.BooleanField(default=False)
    c5=models.BooleanField(default=False)
    c6=models.BooleanField(default=False)
    c7=models.BooleanField(default=False)
    c8=models.BooleanField(default=False)
    c9=models.BooleanField(default=False)
    c10=models.BooleanField(default=False)

    d1=models.BooleanField(default=False)
    d2=models.BooleanField(default=False)
    d3=models.BooleanField(default=False)
    d4=models.BooleanField(default=False)
    d5=models.BooleanField(default=False)
    d6=models.BooleanField(default=False)
    d7=models.BooleanField(default=False)
    d8=models.BooleanField(default=False)
    d9=models.BooleanField(default=False)
    d10=models.BooleanField(default=False)


    def __str__(self):
        return self.movi.name +" | "+ self.time.time +" | "+self.date.date.strftime('%Y-%m-%d')


class Customeuser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.EmailField()
    otp=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.id}"




