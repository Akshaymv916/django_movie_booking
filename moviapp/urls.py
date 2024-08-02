from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('cinema/<int:id>',views.details,name='cinema'),
    path('seat/<int:id>/<int:pk>/<int:pd>/<int:pz>', views.seating, name='seat'),
    path('bookings', views.bookings, name='bookings'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('movibook',views.movibook,name='movibook'),
    path('ticket/<int:id>', views.moviticket, name='ticket'),
    path('dashoboard', views.dashboard, name='dashboard'),
    path('showadd',views.showadd,name='showadd'),
    path('dateadd',views.dateadd,name='dateadd'),
    path('bookingcount',views.bookingcount,name='bookingcount'),
    path('add/<int:id>', views.addshow, name='addshow'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('remove1/<int:id>', views.remove1, name='remove1'),
    path('remove3/<int:id>', views.remove3, name='remove3'),
    path('search',views.search,name='search'),
    path('datetime/<int:id>',views.datetime,name='datetime'),
    path('showdate/<int:id>/<int:pk>',views.showdate,name='showdate'),

    path('adddates',views.adddates,name='adddates'),
    path('seatbooking',views.seatbooking,name='seatbooking'),
    path('seatingadd',views.seatingadd,name='seatingadd'),
    path('bookinginfo',views.bookinginfo,name='bookinginfo'),
    path('bookingverify',views.bookingverify,name='boookingverify'),
    path('verification',views.verification,name='verification'),
    path('otpverify',views.otpverify,name='otpverify'),
    path('paymentsuccess/',views.success,name='paymentsuccess'),
    path('bookingclear',views.bookingclear,name='bookingclear'),




    # path('seat/<int:id>',views.seat,name='seat'),
    # path('booked',views.booked,name='booked'),
    # path('ticket/<int:id>',views.ticket,name='ticket'),

]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
