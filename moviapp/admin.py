
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customeuser)
admin.site.register(Navbar)
admin.site.register(Dates)
admin.site.register(Time)



@admin.register(Cinema)
class CinemaModelAdmin(admin.ModelAdmin):
    list_display=['cinema','movi_name','poster',]


@admin.register(Movie)
class MoviModelAdmin(admin.ModelAdmin):
    list_display=['movie','name','language','genre']



@admin.register(Show)
class ShowModelAdmin(admin.ModelAdmin):
    list_display=['shows','movi','time','date','price']



@admin.register(Seatbook)
class SeatbookModelAdmin(admin.ModelAdmin):
    list_display=['movi','date','time','seatcount']



@admin.register(Bookings)
class BookingModelAdmin(admin.ModelAdmin):
    list_display=['user','shows','seat','time','paymentid','price','paid']
