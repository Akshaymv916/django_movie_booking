from http import client
from itertools import count
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from moviapp.models import Customeuser, Dates, Movie,Navbar,Cinema, Seatbook,Show,Bookings, Time
from datetime import date, datetime
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
import urllib.parse
from django.conf import settings
import razorpay
client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRATE))



def sendotp(mail,otp):
    try:
        otp=otp
        subject='your otp code'
        msg=f'Krishna cineplex | your otp code is {otp}'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[mail]

        send_mail(subject,msg,email_from,recipient_list)
    except:
        print('error')


def get_dates():
    date=Dates.objects.all()
    return date

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    navbar=Navbar.objects.all()
    context = {
        'movie': movies,
        'navbar':navbar
    }
    return render(request,"index.html", context)

def details(request,id):
    movi=Movie.objects.get(movie=id)
    cine = Cinema.objects.filter(cinema_shows__movi=movi).prefetch_related('cinema_shows').distinct()
    show=Show.objects.filter(movi=id)
    context={
        'movi':movi,
        'cine':cine,
        'show':show
    }
    return  render(request,'details.html',context)



def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username/Password is incorrect')
                return redirect('login')
        else:
            return render(request, "login.html")

def signup(request):

        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            phone=request.POST['phone']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exist')
                    return redirect("signup")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already exist')
                    return redirect("signup")
                elif len(phone) != 10:
                    messages.error(request, "Enter a valid number")
                    return redirect("signup")
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    email=email, password=password1)
                    user1=Customeuser(user=user,phonenumber=phone,email=email,name=first_name)
                    user1.save()
                    user.save()
                    messages.info(request, 'User created')
                    return redirect('login')
            else:
                messages.info(request, 'Password not match')
            return redirect('signup')
        else:
            return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def seating(request,id,pk,pd,pz):
    show=Show.objects.get(shows=id)
    date=Dates.objects.get(id=pk)
    seat = Bookings.objects.filter(shows=id)
    movi=Movie.objects.get(movie=pz)

    movibook=Seatbook.objects.get(movi=movi,date=date,time=pd)
    
    return render(request,"seating.html", {'show':show,'seat':seat,'date':date,'movibook':movibook})

def bookingverify(request):
    if request.method == 'POST':
        user=request.user
        phone=Customeuser.objects.get(user=user)
        time=request.POST['movitime']
        timeid=request.POST['movitimeid']
        times=Time.objects.get(id=timeid)
        show=request.POST['show']
        movi_name=request.POST['movi_name']
        movi_nameid=request.POST['movi_nameid']
        movi=Movie.objects.get(movie=movi_nameid)
        amount=request.POST['amount']
        print(show,movi_name,movi)
        dateid=request.POST['movidateid']
        date=request.POST['movidate']
        
        a1=request.POST.get('A1')
        a2=request.POST.get('A2')
        a3=request.POST.get('A3')
        a4=request.POST.get('A4')
        a5=request.POST.get('A5')
        a6=request.POST.get('A6')
        a7=request.POST.get('A7')
        a8=request.POST.get('A8')
        a9=request.POST.get('A9')
        a10=request.POST.get('A10')


        b1=request.POST.get('B1')
        b2=request.POST.get('B2')
        b3=request.POST.get('B3')
        b4=request.POST.get('B4')
        b5=request.POST.get('B5')
        b6=request.POST.get('B6')
        b7=request.POST.get('B7')
        b8=request.POST.get('B8')
        b9=request.POST.get('B9')
        b10=request.POST.get('B10')


        c1=request.POST.get('C1')
        c2=request.POST.get('C2')
        c3=request.POST.get('C3')
        c4=request.POST.get('C4')
        c5=request.POST.get('C5')
        c6=request.POST.get('C6')
        c7=request.POST.get('C7')
        c8=request.POST.get('C8')
        c9=request.POST.get('C9')
        c10=request.POST.get('C10')


        d1=request.POST.get('D1')
        d2=request.POST.get('D2')
        d3=request.POST.get('D3')
        d4=request.POST.get('D4')
        d5=request.POST.get('D5')
        d6=request.POST.get('D6')
        d7=request.POST.get('D7')
        d8=request.POST.get('D8')
        d9=request.POST.get('D9')
        d10=request.POST.get('D10')
        useat = []
        elements = [a1, a2, a3, a4, a5, a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
        for element in elements:
            if element is not None:
                useat.append(element)
        context={
            'useat':useat,
            'amount':amount,
            'time':times,
            'timeid':timeid,
            'movi':movi,
            'phone':phone,
            'movi_nameid':movi_nameid,
            'dateid':dateid,
            'date':date,
            'show':show,

            'A1':a1,'A2':a2,'A3':a3,'A4':a4,'A5':a5,'A6':a6,'A7':a7,'A8':a8,'A9':a9,'A10':a10,
            'B1':b1,'B2':b2,'B3':b3,'B4':b4,'B5':b5,'B6':b6,'B7':b7,'B8':b8,'B9':b9,'B10':b10,
            'C1':c1,'C2':c2,'C3':c3,'C4':c4,'C5':c5,'C6':c6,'C7':c7,'C8':c8,'C9':c9,'C10':c10,
            'D1':d1,'D2':d2,'D3':d3,'D4':d4,'D5':d5,'D6':d6,'D7':d7,'D8':d8,'D9':d9,'D10':d10,


            
        }

        return render(request,'bookingverify.html',context)

def verification(request):
    if request.method=='POST':
        a1=request.POST.get('A1')
        a2=request.POST.get('A2')
        a3=request.POST.get('A3')
        a4=request.POST.get('A4')
        a5=request.POST.get('A5')
        a6=request.POST.get('A6')
        a7=request.POST.get('A7')
        a8=request.POST.get('A8')
        a9=request.POST.get('A9')
        a10=request.POST.get('A10')


        b1=request.POST.get('B1')
        b2=request.POST.get('B2')
        b3=request.POST.get('B3')
        b4=request.POST.get('B4')
        b5=request.POST.get('B5')
        b6=request.POST.get('B6')
        b7=request.POST.get('B7')
        b8=request.POST.get('B8')
        b9=request.POST.get('B9')
        b10=request.POST.get('B10')


        c1=request.POST.get('C1')
        c2=request.POST.get('C2')
        c3=request.POST.get('C3')
        c4=request.POST.get('C4')
        c5=request.POST.get('C5')
        c6=request.POST.get('C6')
        c7=request.POST.get('C7')
        c8=request.POST.get('C8')
        c9=request.POST.get('C9')
        c10=request.POST.get('C10')


        d1=request.POST.get('D1')
        d2=request.POST.get('D2')
        d3=request.POST.get('D3')
        d4=request.POST.get('D4')
        d5=request.POST.get('D5')
        d6=request.POST.get('D6')
        d7=request.POST.get('D7')
        d8=request.POST.get('D8')
        d9=request.POST.get('D9')
        d10=request.POST.get('D10')
        email=request.POST['email']
        user=request.user
        phone=request.POST['mobile']
        mtime=request.POST['mtime']
        mmovi=request.POST['mmovi']
        mdate=request.POST['mdate']
        mdateid=request.POST['mdateid']
        mtimeid=request.POST['mtimeid']
        mmoviid=request.POST['mmoviid']
        mprice=request.POST['mprice']
        mseat=request.POST['mseat']
        show=request.POST['show']
        
        otp = str(random.randint(1000 , 9999))
        user1=Customeuser.objects.get(user=user)
        user1.otp=otp
        sendotp(email,otp)
        user1.save()
        messages.success(request, ",4 digit code send to your email")

        context={
            'useat':mseat,
            'amount':mprice,
            'time':mtime,
            'movi':mmovi,
            'email':email,
            'date':mdate,
            'dateid':mdateid,
            'timeid':mtimeid,
            'moviid':mmoviid,
            'show':show,

            'A1':a1,'A2':a2,'A3':a3,'A4':a4,'A5':a5,'A6':a6,'A7':a7,'A8':a8,'A9':a9,'A10':a10,
            'B1':b1,'B2':b2,'B3':b3,'B4':b4,'B5':b5,'B6':b6,'B7':b7,'B8':b8,'B9':b9,'B10':b10,
            'C1':c1,'C2':c2,'C3':c3,'C4':c4,'C5':c5,'C6':c6,'C7':c7,'C8':c8,'C9':c9,'C10':c10,
            'D1':d1,'D2':d2,'D3':d3,'D4':d4,'D5':d5,'D6':d6,'D7':d7,'D8':d8,'D9':d9,'D10':d10,
        }

    return render(request,'verification.html',context)


def otpverify(request):
    if request.method=='POST':
        a1=request.POST.get('A1')
        a2=request.POST.get('A2')
        a3=request.POST.get('A3')
        a4=request.POST.get('A4')
        a5=request.POST.get('A5')
        a6=request.POST.get('A6')
        a7=request.POST.get('A7')
        a8=request.POST.get('A8')
        a9=request.POST.get('A9')
        a10=request.POST.get('A10')


        b1=request.POST.get('B1')
        b2=request.POST.get('B2')
        b3=request.POST.get('B3')
        b4=request.POST.get('B4')
        b5=request.POST.get('B5')
        b6=request.POST.get('B6')
        b7=request.POST.get('B7')
        b8=request.POST.get('B8')
        b9=request.POST.get('B9')
        b10=request.POST.get('B10')


        c1=request.POST.get('C1')
        c2=request.POST.get('C2')
        c3=request.POST.get('C3')
        c4=request.POST.get('C4')
        c5=request.POST.get('C5')
        c6=request.POST.get('C6')
        c7=request.POST.get('C7')
        c8=request.POST.get('C8')
        c9=request.POST.get('C9')
        c10=request.POST.get('C10')


        d1=request.POST.get('D1')
        d2=request.POST.get('D2')
        d3=request.POST.get('D3')
        d4=request.POST.get('D4')
        d5=request.POST.get('D5')
        d6=request.POST.get('D6')
        d7=request.POST.get('D7')
        d8=request.POST.get('D8')
        d9=request.POST.get('D9')
        d10=request.POST.get('D10')
        otp=request.POST['otp']
        mtime=request.POST['mtime']
        mmovi=request.POST['mmovi']
        mdate=request.POST['mdate']
        mtimeid=request.POST['mtimeid']
        mmoviid=request.POST['mmoviid']
        mdateid=request.POST['mdateid']
        mprice=request.POST['mprice']
        mseat=request.POST['mseat']
        email=request.POST['email']
        show=request.POST['show']

        user=request.user
        user1=Customeuser.objects.get(user=user)
        otpint=int(otp)
        price=int(mprice)
        moviname=Seatbook.objects.get(movi=mmoviid,date=mdateid,time=mtimeid)
        payment = client.order.create({
                    "amount":price * 100,  # Amount in paise for Razorpay
                    "currency": "INR",
                    "payment_capture": "1"
                })
        order_id = payment['id']
        context={
            'useat':mseat,
            'amount':price,
            'time':mtime,
            'movi':mmovi,
            'email':email,
            'date':mdate,
            'user':user1,
            'order_id':order_id,
            'dateid':mdateid,
            'timeid':mtimeid,
            'moviid':mmoviid,
            'show':show,
            
            'A1':a1,'A2':a2,'A3':a3,'A4':a4,'A5':a5,'A6':a6,'A7':a7,'A8':a8,'A9':a9,'A10':a10,
            'B1':b1,'B2':b2,'B3':b3,'B4':b4,'B5':b5,'B6':b6,'B7':b7,'B8':b8,'B9':b9,'B10':b10,
            'C1':c1,'C2':c2,'C3':c3,'C4':c4,'C5':c5,'C6':c6,'C7':c7,'C8':c8,'C9':c9,'C10':c10,
            'D1':d1,'D2':d2,'D3':d3,'D4':d4,'D5':d5,'D6':d6,'D7':d7,'D8':d8,'D9':d9,'D10':d10,
        }
        if user1.otp == otpint:
            if a1 != "None":        
                moviname.a1=True
                moviname.seatcount=moviname.seatcount+1
            if a2 != "None":
                moviname.a2=True
                moviname.seatcount=moviname.seatcount+1
            if a3 != "None":
                moviname.a3=True
                moviname.seatcount=moviname.seatcount+1
            if a4 != "None":
                moviname.a4=True
                moviname.seatcount=moviname.seatcount+1
            if a5 != "None":
                moviname.a5=True
                moviname.seatcount=moviname.seatcount+1
            if a6 != "None":
                moviname.a6=True
                moviname.seatcount=moviname.seatcount+1
            if a7 != "None":
                moviname.seatcount=moviname.seatcount+1
                moviname.a7=True
            if a8 != "None":
                moviname.a8=True
                moviname.seatcount=moviname.seatcount+1
            if a9 != "None":
                moviname.a9=True
                moviname.seatcount=moviname.seatcount+1
            if a10 != "None":
                moviname.a10=True
                moviname.seatcount=moviname.seatcount+1


            if b1 != "None":
                moviname.b1=True
                moviname.seatcount=moviname.seatcount+1
            if b2 != "None":
                moviname.seatcount=moviname.seatcount+1
                moviname.b2=True
            if b3 != "None":
                moviname.b3=True
                moviname.seatcount=moviname.seatcount+1
            if b4 != "None":
                moviname.b4=True
                moviname.seatcount=moviname.seatcount+1
            if b5 != "None":
                moviname.b5=True
                moviname.seatcount=moviname.seatcount+1
            if b6 != "None":
                moviname.b6=True
                moviname.seatcount=moviname.seatcount+1
            if b7 != "None":
                moviname.b7=True
                moviname.seatcount=moviname.seatcount+1
            if b8 != "None":
                moviname.b8=True
                moviname.seatcount=moviname.seatcount+1
            if b9 != "None":
                moviname.b9=True
                moviname.seatcount=moviname.seatcount+1
            if b10 != "None":
                moviname.b10=True
                moviname.seatcount=moviname.seatcount+1


            if c1 != "None":
                moviname.c1=True
                moviname.seatcount=moviname.seatcount+1
            if c2 != "None":
                moviname.c2=True
                moviname.seatcount=moviname.seatcount+1
            if c3 != "None":
                moviname.c3=True
                moviname.seatcount=moviname.seatcount+1
            if c4 != "None":
                moviname.c4=True
                moviname.seatcount=moviname.seatcount+1
            if c5 != "None":
                moviname.c5=True
                moviname.seatcount=moviname.seatcount+1
            if c6 != "None":
                moviname.c6=True
                moviname.seatcount=moviname.seatcount+1
            if c7 != "None":
                moviname.c7=True
                moviname.seatcount=moviname.seatcount+1
            if c8 != "None":
                moviname.c8=True
                moviname.seatcount=moviname.seatcount+1
            if c9 != "None":
                moviname.c9=True
                moviname.seatcount=moviname.seatcount+1
            if c10 != "None":
                moviname.c10=True
                moviname.seatcount=moviname.seatcount+1

            if d1 != "None":
                moviname.d1=True
                moviname.seatcount=moviname.seatcount+1
            if d2 != "None":
                moviname.d2=True
                moviname.seatcount=moviname.seatcount+1
            if d3 != "None":
                moviname.d3=True
                moviname.seatcount=moviname.seatcount+1
            if d4 != "None":
                moviname.d4=True
                moviname.seatcount=moviname.seatcount+1
            if d5 != "None":
                moviname.d5=True
                moviname.seatcount=moviname.seatcount+1
            if d6 != "None":
                moviname.d6=True
                moviname.seatcount=moviname.seatcount+1
            if d7 != "None":
                moviname.d7=True
                moviname.seatcount=moviname.seatcount+1
            if d8 != "None":
                moviname.d8=True
                moviname.seatcount=moviname.seatcount+1
            if d9 != "None":
                moviname.d9=True
                moviname.seatcount=moviname.seatcount+1
            if d10 != "None":
                moviname.d10=True
                moviname.seatcount=moviname.seatcount+1

            moviname.save()
            mtimes=Time.objects.get(id=mtimeid)
            book=Bookings(seat=mseat,shows_id=show,user=user,price=price,time=mtimes,paymentid=order_id,mail=email)
            book.save()
            return render(request,'bookingconform.html',context)
        else:
            messages.error(request,'otp incorrect')
            return render(request,'verification.html',context)
        
@csrf_exempt
def success(request):
            try:
                response=request.POST
                print(response)
                params_dict={
                    'razorpay_payment_id': response['razorpay_payment_id'],
                    'razorpay_order_id': response['razorpay_order_id'],
                    'razorpay_signature': response['razorpay_signature']

                }

                print(params_dict)
                client=razorpay.Client(auth=('rzp_test_MrcFBm65u39qex','HsMWRqSflka9cs5l0EwuyxTZ'))
                try:
                    status=client.utility.verify_payment_signature(params_dict)
                    payment=Bookings.objects.get(paymentid=response['razorpay_order_id'])
                    payment.paymentid=response['razorpay_payment_id']
                    payment.paid=True
                    payment.save()
                    mail=payment.mail
                    seat=payment.seat
                    price=payment.price
                    date=payment.shows.date
                    movi=payment.shows.movi.name
                    send_invoice(mail,movi,price,date,seat)
                    return redirect('bookings')
                except:
                    return render(request,'userprofile/ordertrack.html')
            except:
                  return render(request,'userprofile/paymentfail.html')


def send_invoice(mail, price, date, movie, seat):
    subject = 'Your Booking Confirmation'
    msg = f'Krishna Cineplex | Booking Confirmed\n\nMovie:{price} \nPrice:{date} \nDate: {movie}\nSeat Number: {seat}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail]

    try:
        send_mail(subject, msg, email_from, recipient_list)
    except Exception as e:
        print(f'Error sending email: {e}')



def movibook(request):
    if request.method == 'POST':
        user=request.user
        time=request.POST['movitime']
        times=Time.objects.get(id=time)
        show=request.POST['show']
        movi_name=request.POST['movi_name']
        amount=request.POST['amount']
        print(show)
        date=request.POST['movidate']
        print(date,time)
        moviname=Seatbook.objects.get(movi=movi_name,date=date,time=time)
        
        a1=request.POST.get('A1')
        a2=request.POST.get('A2')
        a3=request.POST.get('A3')
        a4=request.POST.get('A4')
        a5=request.POST.get('A5')
        a6=request.POST.get('A6')
        a7=request.POST.get('A7')
        a8=request.POST.get('A8')
        a9=request.POST.get('A9')
        a10=request.POST.get('A10')


        b1=request.POST.get('B1')
        b2=request.POST.get('B2')
        b3=request.POST.get('B3')
        b4=request.POST.get('B4')
        b5=request.POST.get('B5')
        b6=request.POST.get('B6')
        b7=request.POST.get('B7')
        b8=request.POST.get('B8')
        b9=request.POST.get('B9')
        b10=request.POST.get('B10')


        c1=request.POST.get('C1')
        c2=request.POST.get('C2')
        c3=request.POST.get('C3')
        c4=request.POST.get('C4')
        c5=request.POST.get('C5')
        c6=request.POST.get('C6')
        c7=request.POST.get('C7')
        c8=request.POST.get('C8')
        c9=request.POST.get('C9')
        c10=request.POST.get('C10')


        d1=request.POST.get('D1')
        d2=request.POST.get('D2')
        d3=request.POST.get('D3')
        d4=request.POST.get('D4')
        d5=request.POST.get('D5')
        d6=request.POST.get('D6')
        d7=request.POST.get('D7')
        d8=request.POST.get('D8')
        d9=request.POST.get('D9')
        d10=request.POST.get('D10')
        useat = []
        elements = [a1, a2, a3, a4, a5, a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
        for element in elements:
            if element is not None:
                useat.append(element)

        if a1 is not None:        
            moviname.a1=True
            moviname.seatcount=moviname.seatcount+1
        if a2 is not None:
            moviname.a2=True
            moviname.seatcount=moviname.seatcount+1
        if a3 is not None:
            moviname.a3=True
            moviname.seatcount=moviname.seatcount+1
        if a4 is not None:
            moviname.a4=True
            moviname.seatcount=moviname.seatcount+1
        if a5 is not None:
            moviname.a5=True
            moviname.seatcount=moviname.seatcount+1
        if a6 is not None:
            moviname.a6=True
            moviname.seatcount=moviname.seatcount+1
        if a7 is not None:
            moviname.seatcount=moviname.seatcount+1
            moviname.a7=True
        if a8 is not None:
            moviname.a8=True
            moviname.seatcount=moviname.seatcount+1
        if a9 is not None:
            moviname.a9=True
            moviname.seatcount=moviname.seatcount+1
        if a10 is not None:
            moviname.a10=True
            moviname.seatcount=moviname.seatcount+1


        if b1 is not None:
            moviname.b1=True
            moviname.seatcount=moviname.seatcount+1
        if b2 is not None:
            moviname.seatcount=moviname.seatcount+1
            moviname.b2=True
        if b3 is not None:
            moviname.b3=True
            moviname.seatcount=moviname.seatcount+1
        if b4 is not None:
            moviname.b4=True
            moviname.seatcount=moviname.seatcount+1
        if b5 is not None:
            moviname.b5=True
            moviname.seatcount=moviname.seatcount+1
        if b6 is not None:
            moviname.b6=True
            moviname.seatcount=moviname.seatcount+1
        if b7 is not None:
            moviname.b7=True
            moviname.seatcount=moviname.seatcount+1
        if b8 is not None:
            moviname.b8=True
            moviname.seatcount=moviname.seatcount+1
        if b9 is not None:
            moviname.b9=True
            moviname.seatcount=moviname.seatcount+1
        if b10 is not None:
            moviname.b10=True
            moviname.seatcount=moviname.seatcount+1


        if c1 is not None:
            moviname.c1=True
            moviname.seatcount=moviname.seatcount+1
        if c2 is not None:
            moviname.c2=True
            moviname.seatcount=moviname.seatcount+1
        if c3 is not None:
            moviname.c3=True
            moviname.seatcount=moviname.seatcount+1
        if c4 is not None:
            moviname.c4=True
            moviname.seatcount=moviname.seatcount+1
        if c5 is not None:
            moviname.c5=True
            moviname.seatcount=moviname.seatcount+1
        if c6 is not None:
            moviname.c6=True
            moviname.seatcount=moviname.seatcount+1
        if c7 is not None:
            moviname.c7=True
            moviname.seatcount=moviname.seatcount+1
        if c8 is not None:
            moviname.c8=True
            moviname.seatcount=moviname.seatcount+1
        if c9 is not None:
            moviname.c9=True
            moviname.seatcount=moviname.seatcount+1
        if c10 is not None:
            moviname.c10=True
            moviname.seatcount=moviname.seatcount+1

        if d1 is not None:
            moviname.d1=True
            moviname.seatcount=moviname.seatcount+1
        if d2 is not None:
            moviname.d2=True
            moviname.seatcount=moviname.seatcount+1
        if d3 is not None:
            moviname.d3=True
            moviname.seatcount=moviname.seatcount+1
        if d4 is not None:
            moviname.d4=True
            moviname.seatcount=moviname.seatcount+1
        if d5 is not None:
            moviname.d5=True
            moviname.seatcount=moviname.seatcount+1
        if d6 is not None:
            moviname.d6=True
            moviname.seatcount=moviname.seatcount+1
        if d7 is not None:
            moviname.d7=True
            moviname.seatcount=moviname.seatcount+1
        if d8 is not None:
            moviname.d8=True
            moviname.seatcount=moviname.seatcount+1
        if d9 is not None:
            moviname.d9=True
            moviname.seatcount=moviname.seatcount+1
        if d10 is not None:
            moviname.d10=True
            moviname.seatcount=moviname.seatcount+1

        moviname.save()

        book=Bookings(seat=useat,shows_id=show,user=user,price=amount,time=times)
        book.save()
        books=Bookings.objects.filter(user=user)
        context={
            'book':books,
            
        }
        return render(request,"bookings.html",context)

def bookings(request):
    user=request.user
    books = Bookings.objects.filter(user=user,paid=True).order_by('-id')
    return render(request, "bookings.html", {'book': books})


def moviticket(request, id):
    ticket = Bookings.objects.get(id=id)
    return render(request,"moviticket.html", {'ticket':ticket})


def dashboard(request):
    user=request.user
    movi=Cinema.objects.all()
    return render(request,'dashboard.html',{'movie':movi})





def showadd(request):

    if request.method == 'POST':
        m = request.POST['m']
        k = request.POST['k']
        t = request.POST['t']
        d = request.POST['d']
        p = request.POST['p']
        time=Time.objects.get(time=t)
        date=Dates.objects.get(date=d)
        show = Show(cinema_id=k,movi_id=m, date=date, time=time, price=p)
        show.save()
        messages.success(request, 'Show Added')
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        m = Show.objects.all()
        sh = Movie.objects.all()

        data = {
            'mov':m,
            's':sh
        }
        return render(request,"showadd.html", data)

def adddates(request):
    date=Dates.objects.all
    context={
        'date':date
    }
    return render(request,'adddate.html',context)

def dateadd(request):
    d = request.POST['d']
    date=Dates(date=d)
    date.save()
    messages.success(request,'date added')
    return redirect(request.META.get('HTTP_REFERER'))






def addshow(request,id):
    movi=Show.objects.filter(cinema_id=id)
    m=Cinema.objects.filter(movi_name=id)
    c=Cinema.objects.all()
    s=Movie.objects.all()
    t=Time.objects.all()
    d=Dates.objects.all()
    movi={
        'movi':movi,
        'm':m,
        's':s,
        'c':c,
        't':t,
        'd':d,
    }
    return render(request,'showadd.html',movi)


def seatbooking(request):
    c=Cinema.objects.all()
    s=Movie.objects.all()
    t=Time.objects.all()
    d=Dates.objects.all()
    seat=Seatbook.objects.all()
    movi={
        's':s,
        'c':c,
        't':t,
        'd':d,
        'seat':seat
    }
    return render(request,'seatbooking.html',movi)

def seatingadd(request):
    if request.method == 'POST':
        m = request.POST['m']
        t = request.POST['t']
        d = request.POST['d']
        time=Time.objects.get(time=t)
        movi=Movie.objects.get(movie=m)
        date=Dates.objects.get(date=d)
        show = Seatbook(movi=movi,date=date,time=time)
        show.save()
        messages.success(request, 'seating Added')
        return redirect(request.META.get('HTTP_REFERER'))

def bookinginfo(request):
    booking=Bookings.objects.all()
    context={
        'booking':booking
    }
    return render(request,'bookinginfo.html',context)

def bookingcount(request):
    count=Seatbook.objects.all()
    context={
        'count':count
    }
    return render(request,'bookingcount.html',context)

def bookingclear(request):
    clear=Bookings.objects.all()
    clear.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def remove(request,id):
    shows=Show.objects.get(pk=id)
    shows.delete()
    return redirect('dashboard')

def remove1(request,id):
    date=Dates.objects.get(id=id)
    date.delete()
    return redirect('dashboard')

def remove3(request,id):
    seat=Seatbook.objects.get(id=id)
    seat.delete()
    return redirect('dashboard')


def search(request):
    query = request.GET.get('query')
    movie = Movie.objects.all().filter(Q(name__contains=query) | Q(movi_desc__contains=query))

    context = {
        'movie': movie
    }
    return render(request, 'search.html', context)

def datetime(request,id):
    dates=get_dates()
    movi=Movie.objects.get(movie=id)
    cine = Cinema.objects.filter(cinema_shows__movi=movi).prefetch_related('cinema_shows').distinct()
    d=Dates.objects.all().order_by('id')[:1]
    seatcount=Seatbook.objects.filter(date=d,movi=movi)
    print(d)
    print(seatcount)
            
    show=Show.objects.filter(date=d,movi=movi)
    current_date = date.today()
    context={
        'movi':movi,
        'cine':cine,
        'show':show,
        'dates':dates,
        'c_date':current_date,
        'seatcount':seatcount
    }
    print(cine)
    return render(request,'timedate.html',context)

def showdate(request,id,pk):
    dates=get_dates()
    movi=Movie.objects.get(movie=pk)
    cine = Cinema.objects.filter(cinema_shows__movi=movi).prefetch_related('cinema_shows').distinct()
    show=Show.objects.filter(date=id,movi=movi)
    d=Dates.objects.all().order_by('id')[:1]
    seatcount=Seatbook.objects.filter(date=d,movi=movi)
    current_date = date.today()
    context={
        'movi':movi,
        'cine':cine,
        'show':show,
        'dates':dates,
        'c_date':current_date,
        'seatcount':seatcount
    }
    print(cine)
    return render(request,'timedate.html',context)