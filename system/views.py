from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .models import register
from django.contrib.auth.decorators import login_required
from .models import Deposit,Draw,Win
from django.db.models import Sum
from django.shortcuts import render, redirect
from system.models import register
from random import choice
from datetime import datetime,time


def login(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request, 'signup.html')

def get(request):
    name = request.POST.get('name')
    Email = request.POST.get('email')
    password = request.POST.get('pw')
    conformpassword = request.POST.get('cpw')

    if name and Email and password and conformpassword:
        print("===>")
        if register.objects.filter(Email=Email).exists():
            # return redirect("/signUp")
            print("......")
            error = "Email Already Used!"
            return render(request, 'signup.html', {'error': error})
        else:
            if password==conformpassword:
                register.objects.create(name=name, Email=Email, password=password, conformpassword=conformpassword)
                return redirect("/login")
            else:
                error = "Your Both Passwords Miss Matched!"
                return render(request, 'signup.html', {'error': error})
    

    
    return redirect("/")

def check(request):
    Email = request.POST.get('Email')
    print(Email)
    password = request.POST.get('password')
    print(password)
    if Email and password:
        user = register.objects.filter(Email=Email, password=password).first()
        if user:
            request.session['sId'] = user.id
            return redirect("/pay")
        
        else:
            error = "Your Passwords Miss Matched!"
            return render(request, 'login.html', {'error': error})

    return redirect("/")

def userFound(request):
    if'sId' in request.session:
        sid = request.session['sId']
        if sid:
            return render(request, "successfull.html", {"sessionId": sid})

    return redirect('/login')

def logout(request):
    if request.method == 'GET':
        delid = request.GET.get('delid')
        if delid:
            del request.session['sId']
    return redirect('/login')

# views.py
def draw(request):
    users = Deposit.objects.all()
    total_amount = Deposit.objects.aggregate(total_amount=Sum('rupee'))['total_amount']
    return render(request,"draw.html",{"Participants" : users,"data": users,"total" : total_amount})
def pay(request):
    # my_time = time(17, 0)  # 5:00 PMme
    # timestamp = datetime.combine(datetime.today(), my_time)
    # pwithdrawal_time = time(17, 0, 0)
    # print("okokk",timestamp)
    # print("okokoko",pwithdrawal_time)

    total_amount = Deposit.objects.aggregate(total_amount=Sum('rupee'))['total_amount']
    print("=-=-=-=-=-=",total_amount)
    current_datetime = datetime.now()
    date = current_datetime.date()
    print("====>",date)
    time = current_datetime.time()
    if 'sId' in request.session:
        sid = request.session['sId']
        d=Deposit.objects.filter(userid=sid,date=date).first()
        c=Draw.objects.filter(userid=sid,date=date).first()
        print("d value ===",d)
        if d is None:
            if "rupee" in request.GET: 
                print("=====================")  
                Deposit.objects.create(userid = sid,date=date, time=time)
                Draw.objects.create(userid = sid,date=date, time=time)
                return redirect("/pay") 
            else:
                print("====--")
        data = register.objects.get(id=sid)
        transaction = Deposit.objects.filter(userid = sid)  
        date=Win.objects.filter(date=date).first()
        datte1=date.date
        print("asdfghjkl==",datte1)
        if(total_amount!=0):
            a="not winner availble"
        else:
            a="yes draw"

        return render(request, "deposite.html", {"Transactions": transaction, "data": data,"total_amount":total_amount,"a":a,"datte1":datte1})

    return redirect("/userFound")
import random
def win(request):
    total_users = register.objects.count()
    random_index = random.randint(0, total_users - 1)
    random_user = register.objects.all()[random_index]
    userid=random_user.id
    print("user==",random_user.id)
    total_amount = Deposit.objects.aggregate(total_amount=Sum('rupee'))['total_amount']
    print("=-=-=-=-=-=",total_amount)
    if total_amount:
        eight=total_amount*80/100
        print("eight",eight)
        print("total_amount",total_amount)
        fifteen=total_amount*15/100
        print("fifteen",fifteen)
        five=total_amount*5/100
        print("five==",five)
        total_amount=total_amount-total_amount
        print(total_amount)
        current_datetime = datetime.now()
        datte1 = current_datetime.date()
        print("====>",datte1)
        if total_amount==0:
            a="congratulations winner is announce"
        else:
            a="no all"
        if eight and fifteen and five:
            total_amount_returned = total_amount + (1000 * (total_amount // 10))
            Win.objects.create(total=total_amount_returned,userid=userid,eight=eight,five=five,fifty=fifteen,date=datte1)
    return render(request,"deposite.html",{'eight':eight,'fifteen':fifteen,'five':five,'total_amount':total_amount,"userid":userid,"a":a,"datte1":datte1})
    

