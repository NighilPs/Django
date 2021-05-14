from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from datetime import date


# Create your views here.

today = date.today()


def home(request):
    return render(request,'home.html')

def book(request):
    data = DocDetails.objects.all
    return render(request, 'book.html', {'d': data})

def comment(request):
    name = request.POST['name']
    email = request.POST['email']
    comm = request.POST['cmd']
    data = Comments(name=name, email=email, comments=comm)
    data.save()
    return render(request, 'home.html')

def sign(request):
    return render(request,'sign.html')

def sub(request):
    name = request.POST['name']
    email = request.POST['email']
    phn = request.POST['phn']
    dob = request.POST['dob']
    pwd = request.POST['pwd']
    data = Sign(name=name,email=email,phn=phn,dob=dob,password=pwd)
    data.save()
    return render(request,'home.html')

def login(request):
    try:
        usernam = request.POST['username']
        request.session['uname'] = usernam
        passw = request.POST['password']
        e = Sign.objects.get(email=usernam)
        if e.password == passw:
            data = DocDetails.objects.all
            return render(request, 'book.html', {'d': data})
        else:
            return HttpResponse("Wrong Password")
    except:
        return HttpResponse("Wrong username")

def submit(request):
    usrname=request.session['uname']
    ida = request.session['docname']
    e = Sign.objects.get(email=usrname)
    name = e.name
    email = e.email
    phn = e.phn
    dob = e.dob
    date = request.POST['date']
    stime = request.POST['stime']
    etime = request.POST['etime']
    symp = request.POST['sym']
    data = Patients(ida=ida,name=name,email=email,phn=phn,dob=dob,date=date,start=stime,end=etime,sym=symp)
    data.save()
    return render(request,'home.html')

def new(request):
    return render(request,'booking.html')

def old_bookings(request):
    request.session['old'] = request.POST['ida']
    return render(request,'oldbooking.html')

def old(request):
    data = Patients.objects.filter(email=request.session['uname'])
    return render(request,'bookings.html',{'d':data})

def oldsubmit(request):
    data = Patients.objects.get(id=request.session['old'])
    ida = request.session['docname']
    date = request.POST['date']
    startt = request.POST['stime']
    endt = request.POST['etime']
    newdata = Patients(ida=ida,name=data.name,email=data.email,phn=data.phn,dob=data.dob,date=date,start=startt,end=endt,sym=data.sym,pres=data.pres)
    newdata.save()
    return render(request,'home.html')

def doc(request):
    return render(request,'doc.html')

def doclogin(request):
    try:
        name = request.POST['name']
        passw = request.POST['pass']
        request.session['docname'] = name
        e = DocLogin.objects.get(dname=name)
        if e.dpass == passw:
            data = Patients.objects.filter(ida=name)
            return render(request,'doclogin.html',{'d':data})
        else:
            return HttpResponse("Wrong Password")
    except:
        return HttpResponse("Wrong username")


def logout(request):
    return render(request,'home.html')

def profile(request):
    name=request.POST['name']
    data=DocDetails.objects.filter(name=name)
    return render(request,'docprofile.html',{'d':data})

def appoinment(request):
    request.session['docname']=request.POST['book']
    return render(request, 'bookbutton.html')


def edit(request):
    id = request.POST['view']
    ida = Patients.objects.get(id=id)
    return render(request,'view.html',{'d':ida})

def save(request):
    ida = request.POST['id']
    presc = request.POST['pre']
    data = Patients.objects.filter(id=ida).update(pres=presc)
    name = request.session['docname']
    data = Patients.objects.filter(ida=name)
    return render(request, 'doclogin.html', {'d': data})

def today_booking(request):
    name = request.session['docname']
    data = Patients.objects.filter(ida=name,date=today)
    return render(request,'today.html',{'d':data})

def all(request):
    name = request.session['docname']
    data = Patients.objects.filter(ida=name)
    return render(request, 'doclogin.html', {'d': data})

def date(request):
    name = request.session['docname']
    data = Patients.objects.filter(ida=name,date=request.POST['date'])
    return render(request, 'today.html', {'d': data})